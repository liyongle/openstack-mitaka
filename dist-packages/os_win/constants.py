# Copyright 2012 Cloudbase Solutions Srl
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""
Hyper-V / Windows related constants.
"""

HYPERV_VM_STATE_OTHER = 1
HYPERV_VM_STATE_ENABLED = 2
HYPERV_VM_STATE_DISABLED = 3
HYPERV_VM_STATE_SHUTTING_DOWN = 4
HYPERV_VM_STATE_REBOOT = 10
HYPERV_VM_STATE_PAUSED = 32768
HYPERV_VM_STATE_SUSPENDED = 32769


WMI_JOB_STATUS_STARTED = 4096
WMI_JOB_STATE_RUNNING = 4
WMI_JOB_STATE_COMPLETED = 7

VM_SUMMARY_NUM_PROCS = 4
VM_SUMMARY_ENABLED_STATE = 100
VM_SUMMARY_MEMORY_USAGE = 103
VM_SUMMARY_UPTIME = 105


ARCH_I686 = 0
ARCH_MIPS = 1
ARCH_ALPHA = 2
ARCH_PPC = 3
ARCH_ARMV7 = 5
ARCH_IA64 = 6
ARCH_X86_64 = 9


PROCESSOR_FEATURE = {
    3: 'mmx',
    6: 'sse',
    7: '3dnow',
    8: 'rdtsc',
    9: 'pae',
    10: 'sse2',
    12: 'nx',
    13: 'sse3',
    17: 'xsave',
    20: 'slat',
    21: 'vmx',
}


CTRL_TYPE_IDE = "IDE"
CTRL_TYPE_SCSI = "SCSI"

DISK = "VHD"
DISK_FORMAT = DISK
DVD = "DVD"
DVD_FORMAT = "ISO"
VOLUME = "VOLUME"

DISK_FORMAT_MAP = {
    DISK_FORMAT.lower(): DISK,
    DVD_FORMAT.lower(): DVD
}

DISK_FORMAT_VHD = "VHD"
DISK_FORMAT_VHDX = "VHDX"

VHD_TYPE_FIXED = 2
VHD_TYPE_DYNAMIC = 3
VHD_TYPE_DIFFERENCING = 4

SCSI_CONTROLLER_SLOTS_NUMBER = 64
IDE_CONTROLLER_SLOTS_NUMBER = 2

_BDI_DEVICE_TYPE_TO_DRIVE_TYPE = {'disk': DISK,
                                  'cdrom': DVD}


HOST_POWER_ACTION_SHUTDOWN = "shutdown"
HOST_POWER_ACTION_REBOOT = "reboot"
HOST_POWER_ACTION_STARTUP = "startup"

IMAGE_PROP_VM_GEN = "hw_machine_type"
IMAGE_PROP_VM_GEN_1 = "hyperv-gen1"
IMAGE_PROP_VM_GEN_2 = "hyperv-gen2"

VM_GEN_1 = 1
VM_GEN_2 = 2

JOB_STATE_COMPLETED = 7
JOB_STATE_TERMINATED = 8
JOB_STATE_KILLED = 9
JOB_STATE_COMPLETED_WITH_WARNINGS = 32768

# Special vlan_id value in ovs_vlan_allocations table indicating flat network
FLAT_VLAN_ID = -1
TRUNK_ENDPOINT_MODE = 5

TYPE_FLAT = 'flat'
TYPE_LOCAL = 'local'
TYPE_VLAN = 'vlan'

SERIAL_CONSOLE_BUFFER_SIZE = 4 << 10
MAX_CONSOLE_LOG_FILE_SIZE = 1 << 19  # 512kB

BOOT_DEVICE_FLOPPY = 0
BOOT_DEVICE_CDROM = 1
BOOT_DEVICE_HARDDISK = 2
BOOT_DEVICE_NETWORK = 3

ISCSI_NO_AUTH_TYPE = 0
ISCSI_CHAP_AUTH_TYPE = 1
ISCSI_MUTUAL_CHAP_AUTH_TYPE = 2

REMOTEFX_MAX_RES_1024x768 = "1024x768"
REMOTEFX_MAX_RES_1280x1024 = "1280x1024"
REMOTEFX_MAX_RES_1600x1200 = "1600x1200"
REMOTEFX_MAX_RES_1920x1200 = "1920x1200"
REMOTEFX_MAX_RES_2560x1600 = "2560x1600"
REMOTEFX_MAX_RES_3840x2160 = "3840x2160"

IPV4_DEFAULT = '0.0.0.0'
