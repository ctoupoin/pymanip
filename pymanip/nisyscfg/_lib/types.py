"""

Types used by NI System Configuration

"""

import ctypes
from pymanip.nisyscfg._lib.constants import NISysCfgResourceProperty as rp
from pymanip.nisyscfg._lib.constants import NISYSCFG_SIMPLE_STRING_LENGTH

NISysCfgEnumExpertHandle = ctypes.c_void_p
NISysCfgSessionHandle = ctypes.c_void_p
NISysCfgBool = ctypes.c_int
NISysCfgBusType = ctypes.c_int
NISysCfgHasDriverType = ctypes.c_int
NISysCfgIsPresentType = ctypes.c_int
NISysCfgTimestampUTC = ctypes.c_uint32 * 4
NISysCfgFirmwareUpdateMode = ctypes.c_int
NISysCfgAccessType = ctypes.c_int

# property: (attr_ctype, attr_ini, create_func, ref_func, enum_class)
NISysCfgResourcePropertyType = {
    rp.IsDevice: (NISysCfgBool, 0, None, ctypes.byref, None),
    rp.IsChassis: (NISysCfgBool, 0, None, ctypes.byref, None),
    rp.ConnectsToBusType: (NISysCfgBusType, 0, None, ctypes.byref, None),
    rp.VendorId: (ctypes.c_uint, 0, None, ctypes.byref, None),
    rp.VendorName: (
        ctypes.c_char_p,
        NISYSCFG_SIMPLE_STRING_LENGTH,
        ctypes.create_string_buffer,
        lambda x: x,
        None,
    ),
    rp.ProductId: (ctypes.c_uint, 0, None, ctypes.byref, None),
    rp.ProductName: (
        ctypes.c_char_p,
        NISYSCFG_SIMPLE_STRING_LENGTH,
        ctypes.create_string_buffer,
        lambda x: x,
        None,
    ),
    rp.SerialNumber: (
        ctypes.c_char_p,
        NISYSCFG_SIMPLE_STRING_LENGTH,
        ctypes.create_string_buffer,
        lambda x: x,
        None,
    ),
    rp.FirmwareRevision: (
        ctypes.c_char_p,
        NISYSCFG_SIMPLE_STRING_LENGTH,
        ctypes.create_string_buffer,
        lambda x: x,
        None,
    ),
    rp.IsNIProduct: (NISysCfgBool, 0, None, ctypes.byref, None),
    rp.IsSimulated: (NISysCfgBool, 0, None, ctypes.byref, None),
    rp.ConnectsToLinkName: (
        ctypes.c_char_p,
        NISYSCFG_SIMPLE_STRING_LENGTH,
        ctypes.create_string_buffer,
        lambda x: x,
        None,
    ),
    rp.HasDriver: (NISysCfgHasDriverType, 0, None, ctypes.byref, None),
    rp.IsPresent: (NISysCfgIsPresentType, 0, None, ctypes.byref, None),
    rp.SlotNumber: (ctypes.c_int, 0, None, ctypes.byref, None),
    rp.SupportsInternalCalibration: (NISysCfgBool, 0, None, ctypes.byref, None),
    rp.InternalCalibrationLastTime: (
        NISysCfgTimestampUTC,
        [0, 0, 0, 0],
        None,
        ctypes.byref,
        None,
    ),
    rp.InternalCalibrationLastTemp: (ctypes.c_double, 0.0, None, ctypes.byref, None),
    rp.SupportsExternalCalibration: (NISysCfgBool, 0, None, ctypes.byref, None),
    rp.ExternalCalibrationLastTemp: (ctypes.c_double, 0.0, None, ctypes.byref, None),
    rp.CalibrationComments: (
        ctypes.c_char_p,
        NISYSCFG_SIMPLE_STRING_LENGTH,
        ctypes.create_string_buffer,
        lambda x: x,
        None,
    ),
    rp.CurrentTemp: (ctypes.c_double, 0.0, None, ctypes.byref, None),
    rp.PxiPciBusNumber: (ctypes.c_uint, 0, None, ctypes.byref, None),
    rp.PxiPciDeviceNumber: (ctypes.c_uint, 0, None, ctypes.byref, None),
    rp.PxiPciFunctionNumber: (ctypes.c_uint, 0, None, ctypes.byref, None),
    rp.PxiPciLinkWidth: (ctypes.c_int, 0, None, ctypes.byref, None),
    rp.PxiPciMaxLinkWidth: (ctypes.c_int, 0, None, ctypes.byref, None),
    rp.UsbInterface: (ctypes.c_uint, 0, None, ctypes.byref, None),
    rp.TcpHostName: (
        ctypes.c_char_p,
        NISYSCFG_SIMPLE_STRING_LENGTH,
        ctypes.create_string_buffer,
        lambda x: x,
        None,
    ),
    rp.TcpMacAddress: (
        ctypes.c_char_p,
        NISYSCFG_SIMPLE_STRING_LENGTH,
        ctypes.create_string_buffer,
        lambda x: x,
        None,
    ),
    rp.TcpIpAddress: (
        ctypes.c_char_p,
        NISYSCFG_SIMPLE_STRING_LENGTH,
        ctypes.create_string_buffer,
        lambda x: x,
        None,
    ),
    rp.TcpDeviceClass: (
        ctypes.c_char_p,
        NISYSCFG_SIMPLE_STRING_LENGTH,
        ctypes.create_string_buffer,
        lambda x: x,
        None,
    ),
    rp.GpibPrimaryAddress: (ctypes.c_int, 0, None, ctypes.byref, None),
    rp.GpibSecondaryAddress: (ctypes.c_int, 0, None, ctypes.byref, None),
    rp.ProvidesBusType: (NISysCfgBusType, 0, None, ctypes.byref, None),
    rp.ProvidesLinkName: (
        ctypes.c_char_p,
        NISYSCFG_SIMPLE_STRING_LENGTH,
        ctypes.create_string_buffer,
        lambda x: x,
        None,
    ),
    rp.NumberOfSlots: (ctypes.c_int, 0, None, ctypes.byref, None),
    rp.SupportsFirmwareUpdate: (NISysCfgBool, 0, None, ctypes.byref, None),
    rp.FirmwareFilePattern: (
        ctypes.c_char_p,
        NISYSCFG_SIMPLE_STRING_LENGTH,
        ctypes.create_string_buffer,
        lambda x: x,
        None,
    ),
    rp.RecommendedCalibrationInterval: (ctypes.c_int, 0, None, ctypes.byref, None),
    rp.SupportsCalibrationWrite: (NISysCfgBool, 0, None, ctypes.byref, None),
    rp.HardwareRevision: (
        ctypes.c_char_p,
        NISYSCFG_SIMPLE_STRING_LENGTH,
        ctypes.create_string_buffer,
        lambda x: x,
        None,
    ),
    rp.CpuModelName: (
        ctypes.c_char_p,
        NISYSCFG_SIMPLE_STRING_LENGTH,
        ctypes.create_string_buffer,
        lambda x: x,
        None,
    ),
    rp.CpuSteppingRevision: (ctypes.c_int, 0, None, ctypes.byref, None),
    # rp.FirmwareUpdateMode: NISysCfgFirmwareUpdateMode,
    # rp.ExternalCalibrationLastTime: NISysCfgTimestampUTC,
    # rp.RecommendedNextCalibrationTime: NISysCfgTimestampUTC,
    rp.CalibrationCurrentPassword: (
        ctypes.c_char_p,
        NISYSCFG_SIMPLE_STRING_LENGTH,
        ctypes.create_string_buffer,
        lambda x: x,
        None,
    ),
    rp.CalibrationNewPassword: (
        ctypes.c_char_p,
        NISYSCFG_SIMPLE_STRING_LENGTH,
        ctypes.create_string_buffer,
        lambda x: x,
        None,
    ),
    # rp.SysCfgAccess: NISysCfgAccessType,
    # rp.AdapterType: NISysCfgAdapterType,
    rp.MacAddress: (
        ctypes.c_char_p,
        NISYSCFG_SIMPLE_STRING_LENGTH,
        ctypes.create_string_buffer,
        lambda x: x,
        None,
    ),
    # rp.AdapterMode: NISysCfgAdapterMode,
    # rp.TcpIpRequestMode: NISysCfgIpAddressMode,
    rp.TcpIpv4Address: (
        ctypes.c_char_p,
        NISYSCFG_SIMPLE_STRING_LENGTH,
        ctypes.create_string_buffer,
        lambda x: x,
        None,
    ),
    rp.TcpIpv4Subnet: (
        ctypes.c_char_p,
        NISYSCFG_SIMPLE_STRING_LENGTH,
        ctypes.create_string_buffer,
        lambda x: x,
        None,
    ),
    rp.TcpIpv4Gateway: (
        ctypes.c_char_p,
        NISYSCFG_SIMPLE_STRING_LENGTH,
        ctypes.create_string_buffer,
        lambda x: x,
        None,
    ),
    rp.TcpIpv4DnsServer: (
        ctypes.c_char_p,
        NISYSCFG_SIMPLE_STRING_LENGTH,
        ctypes.create_string_buffer,
        lambda x: x,
        None,
    ),
    # rp.TcpPreferredLinkSpeed: NISysCfgLinkSpeed,
    # rp.TcpCurrentLinkSpeed: NISysCfgLinkSpeed,
    # rp.TcpPacketDetection: NISysCfgPacketDetection,
    rp.TcpPollingInterval: (ctypes.c_uint, 0, None, ctypes.byref, None),
    rp.IsPrimaryAdapter: (NISysCfgBool, 0, None, ctypes.byref, None),
    rp.EtherCatMasterId: (ctypes.c_uint, 0, None, ctypes.byref, None),
    rp.EtherCatMasterRedundancy: (NISysCfgBool, 0, None, ctypes.byref, None),
    rp.WlanBssid: (
        ctypes.c_char_p,
        NISYSCFG_SIMPLE_STRING_LENGTH,
        ctypes.create_string_buffer,
        lambda x: x,
        None,
    ),
    rp.WlanCurrentLinkQuality: (ctypes.c_uint, 0, None, ctypes.byref, None),
    rp.WlanCurrentSsid: (
        ctypes.c_char_p,
        NISYSCFG_SIMPLE_STRING_LENGTH,
        ctypes.create_string_buffer,
        lambda x: x,
        None,
    ),
    # rp.WlanCurrentConnectionType: NISysCfgConnectionType,
    # rp.WlanCurrentSecurityType: NISysCfgSecurityType,
    # rp.WlanCurrentEapType: NISysCfgEapType,
    rp.WlanCountryCode: (ctypes.c_int, 0, None, ctypes.byref, None),
    rp.WlanChannelNumber: (ctypes.c_uint, 0, None, ctypes.byref, None),
    rp.WlanClientCertificate: (
        ctypes.c_char_p,
        NISYSCFG_SIMPLE_STRING_LENGTH,
        ctypes.create_string_buffer,
        lambda x: x,
        None,
    ),
    rp.WlanSecurityIdentity: (
        ctypes.c_char_p,
        NISYSCFG_SIMPLE_STRING_LENGTH,
        ctypes.create_string_buffer,
        lambda x: x,
        None,
    ),
    rp.WlanSecurityKey: (
        ctypes.c_char_p,
        NISYSCFG_SIMPLE_STRING_LENGTH,
        ctypes.create_string_buffer,
        lambda x: x,
        None,
    ),
    # rp.SystemStartTime: NISysCfgTimestampUTC ,
    # rp.CurrentTime: NISysCfgTimestampUTC,
    rp.TimeZone: (
        ctypes.c_char_p,
        NISYSCFG_SIMPLE_STRING_LENGTH,
        ctypes.create_string_buffer,
        lambda x: x,
        None,
    ),
    rp.UserDirectedSafeModeSwitch: (NISysCfgBool, 0, None, ctypes.byref, None),
    rp.ConsoleOutSwitch: (NISysCfgBool, 0, None, ctypes.byref, None),
    rp.IpResetSwitch: (NISysCfgBool, 0, None, ctypes.byref, None),
    rp.NumberOfDiscoveredAccessPoints: (ctypes.c_uint, 0, None, ctypes.byref, None),
    rp.NumberOfExperts: (ctypes.c_int, 0, None, ctypes.byref, None),
    rp.NumberOfServices: (ctypes.c_int, 0, None, ctypes.byref, None),
    rp.NumberOfAvailableFirmwareVersions: (ctypes.c_int, 0, None, ctypes.byref, None),
    rp.NumberOfCpus: (ctypes.c_int, 0, None, ctypes.byref, None),
    rp.NumberOfFans: (ctypes.c_int, 0, None, ctypes.byref, None),
    rp.NumberOfTemperatureSensors: (ctypes.c_int, 0, None, ctypes.byref, None),
    rp.NumberOfVoltageSensors: (ctypes.c_int, 0, None, ctypes.byref, None),
    rp.NumberOfUserLedIndicators: (ctypes.c_int, 0, None, ctypes.byref, None),
    rp.NumberOfUserSwitches: (ctypes.c_int, 0, None, ctypes.byref, None),
}
