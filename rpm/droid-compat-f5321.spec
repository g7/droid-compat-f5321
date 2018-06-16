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
%define divert_system_override_copy "/usr/lib/droid-compat/system/etc/sensors/sensor_def_qcomdev.conf"

%define dtb_package droid-devicetree-f5321

%include droid-compat-device/droid-compat-device.inc

### (TEMPORARY) SENSORS QUIRKS ###

%define disabled_sensors libhybrisgyroscopeadaptor-qt5.so libhybrismagnetometeradaptor-qt5.so libhybrispressureadaptor-qt5.so libhybrisstepcounteradaptor-qt5.so

%package hybris-libsensorfw-qt5
Summary: Quirks for hybris-libsensorfw-qt5
Requires: hybris-libsensorfw-qt5

%description hybris-libsensorfw-qt5
%{summary}.

%files hybris-libsensorfw-qt5

%post hybris-libsensorfw-qt5
for diversion in %{disabled_sensors}; do
	diversion="/usr/lib/sensord-qt5/${diversion}"
	rpm-divert add \
		droid-compat-%{device}-hybris-libsensorfw-qt5 \
		${diversion} \
		/var/lib/diversions/${diversion}.diverted
done

rpm-divert apply --package droid-compat-%{rpm_device}-hybris-libsensorfw-qt5 --create-directory

%preun hybris-libsensorfw-qt5
if [ $1 -eq 0 ]; then
	# As on RPM-based systems the installation scriptlets of the upgrade
	# are executed _before_ removing the old version (thus executing this
	# postun scriplet at the end of the transaction), we are going to
	# unapply the diversions only on package removals.
	rpm-divert unapply --package droid-compat-%{rpm_device}-hybris-libsensorfw-qt5

	for diversion in %{disabled_sensors}; do
		diversion="/usr/lib/sensord-qt5/${diversion}"
		rpm-divert remove \
			droid-compat-%{rpm_device}-hybris-libsensorfw-qt5 \
			${diversion}
	done

fi

%triggerin hybris-libsensorfw-qt5 -- hybris-libsensorfw-qt5
if [ $2 -gt 1 ]; then
	# On upgrades, unapply the triggers so that when rpm will put the
	# upgraded files back in will not overwrite the diversion symlinks
	rpm-divert unapply --package droid-compat-%{rpm_device}-hybris-libsensorfw-qt5
fi

%triggerun hybris-libsensorfw-qt5 -- hybris-libsensorfw-qt5
if [ $1 -gt 0 ] && [ $2 -gt 0 ]; then
	# Now that the upgrade files are in their place, it is time to re-apply
	# the diversions
	rpm-divert apply --package droid-compat-%{rpm_device}-hybris-libsensorfw-qt5 --create-directory
fi
