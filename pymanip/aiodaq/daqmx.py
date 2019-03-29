"""

Concrete implementation with nidaqmx-python

"""

import asyncio
import time

import numpy as np

from nidaqmx import Task
from nidaqmx.constants import READ_ALL_AVAILABLE
from nidaqmx.errors import DaqError
from nidaqmx.constants import TerminalConfiguration

from pymanip.aiodaq import TerminalConfig, TriggerConfig, AcquisitionCard

ConcreteTerminalConfig = {
    TerminalConfig.RSE: TerminalConfiguration.RSE,
    TerminalConfig.NRSE: TerminalConfiguration.NRSE,
    TerminalConfig.Diff: TerminalConfiguration.DIFFERENTIAL,
    TerminalConfig.PseudoDiff: TerminalConfiguration.PSEUDODIFFERENTIAL
}


class DAQmxSystem(AcquisitionCard):

    def __init__(self):
        super(DAQmxSystem, self).__init__()
        self.task = Task()
        self.reading = False

    @property
    def samp_clk_max_rate(self):
        return self.task.timing.samp_clk_max_rate

    def close(self):
        if self.task:
            self.channels = []
            self.task.close()
            self.task = None

    def add_channel(self, channel_name, terminal_config, voltage_range):
        tc = ConcreteTerminalConfig[terminal_config]
        ai_chan = self.task.ai_channels.add_ai_voltage(channel_name,
                                                       terminal_config=tc,
                                                       min_val=-voltage_range,
                                                       max_val=voltage_range)
        self.channels.append(ai_chan)

    def configure_clock(self, sample_rate, samples_per_chan):
        self.task.timing.cfg_samp_clk_timing(sample_rate,
                                             samps_per_chan=samples_per_chan)
        self.sample_rate = sample_rate
        self.samples_per_chan = samples_per_chan

    def configure_trigger(self, trigger_source=None, trigger_level=0,
                          trigger_config=TriggerConfig.EdgeRising):

        st = self.task.triggers.start_trigger
        if trigger_source is None:
            st.disable_start_trig()
        else:
            if trigger_config != TriggerConfig.EdgeRising:
                raise NotImplementedError()
            st.cfg_anlg_edge_start_trig(trigger_source, trigger_level)

    def start(self):
        self.task.start()
        self.running = True

    async def stop(self):
        self.running = False
        while self.reading:
            await asyncio.sleep(1.0)
        self.task.stop()

    async def read(self):
        self.reading = True
        done = False
        while self.running:
            try:
                await self.loop.run_in_executor(None,
                                                self.task.wait_until_done,
                                                1.0)
            except DaqError:
                continue
            done = True
            break
        if done and self.running:
            data = await self.loop.run_in_executor(None,
                                                   self.task.read,
                                                   READ_ALL_AVAILABLE)
            self.last_read = time.monotonic()
            data = np.array(data)
        else:
            data = None
        self.reading = False
        return data