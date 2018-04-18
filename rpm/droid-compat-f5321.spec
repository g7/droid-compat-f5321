# The real device details.
%define device f5321
%define device_codename kugo

# The device details of the actual HW adaptation we rely upon
%define adaptation_device f5121
%define adaptation_device_codename suzu
#define adaptation_device f5321
#define adaptation_device_codename kugo

# Various settings
%define patch_kernel 1
%define custom_cmdline "lpm_levels.sleep_disabled=1 user_debug=31 androidboot.selinux=permissive msm_rtb.filter=0x3F ehci-hcd.park=3 dwc3.maximum_speed=high dwc3_msm.prop_chg_detect=Y coherent_pool=8M sched_enable_power_aware=1 androidboot.hardware=kugo zram.num_devices=4"
%define custom_dtb "/usr/lib/devicetrees/msm8956-loire-kugo_generic.dtb"

%define divert_flash_partition_device_info 1
%define custom_flash_partition_device_info_path "/usr/lib/droid-compat/flash-partition/device-info"

%define divert_system 1

%define dtb_package droid-devicetree-f5321

%include droid-compat-device/droid-compat-device.inc
