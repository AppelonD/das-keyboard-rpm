# Don't try fancy stuff like debuginfo, which is useless on binary-only
# packages. Don't strip binary too
# Be sure buildpolicy set to do nothing
%define        __spec_install_post %{nil}
%define          debug_package %{nil}
%define        __os_install_post %{_dbpath}/brp-compress

Summary: Qapp Tools
Name: das-keyboard-q
Version: 3.1.0
Release: 11
License: CC BY 4.0
Group: keyboard
SOURCE0 : %{name}-%{version}.tar.gz
URL: https://www.daskeyboard.io/

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%{?systemd_requires}
BuildRequires: systemd

%description
The Qapp RPM is build from the *.deb released by the daskeyboard.

%post
%systemd_post das_keyboard_q-service.service

%preun
%systemd_preun das_keyboard_q-service.service

%postun
%systemd_postun_with_restart das_keyboard_q-service.service

%prep
%setup -q

%build
# Empty section.

%install
rm -rf %{buildroot}
mkdir -p  %{buildroot}

# in builddir
cp -a * %{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
/etc/systemd/system
/etc/systemd/system/das_keyboard_q-service.service
/etc/udev/rules.d
/etc/udev/rules.d/99-daskeyboard.rules
/usr/bin/das-keyboard-q
/usr/lib/das-keyboard-q
/usr/lib/das-keyboard-q/LICENSES.chromium.html
/usr/lib/das-keyboard-q/blink_image_resources_200_percent.pak
/usr/lib/das-keyboard-q/content_resources_200_percent.pak
/usr/lib/das-keyboard-q/content_shell.pak
/usr/lib/das-keyboard-q/das-keyboard-q
/usr/lib/das-keyboard-q/icudtl.dat
/usr/lib/das-keyboard-q/libffmpeg.so
/usr/lib/das-keyboard-q/libnode.so
/usr/lib/das-keyboard-q/locales
/usr/lib/das-keyboard-q/locales/am.pak
/usr/lib/das-keyboard-q/locales/ar.pak
/usr/lib/das-keyboard-q/locales/bg.pak
/usr/lib/das-keyboard-q/locales/bn.pak
/usr/lib/das-keyboard-q/locales/ca.pak
/usr/lib/das-keyboard-q/locales/cs.pak
/usr/lib/das-keyboard-q/locales/da.pak
/usr/lib/das-keyboard-q/locales/de.pak
/usr/lib/das-keyboard-q/locales/el.pak
/usr/lib/das-keyboard-q/locales/en-GB.pak
/usr/lib/das-keyboard-q/locales/en-US.pak
/usr/lib/das-keyboard-q/locales/es-419.pak
/usr/lib/das-keyboard-q/locales/es.pak
/usr/lib/das-keyboard-q/locales/et.pak
/usr/lib/das-keyboard-q/locales/fa.pak
/usr/lib/das-keyboard-q/locales/fake-bidi.pak
/usr/lib/das-keyboard-q/locales/fi.pak
/usr/lib/das-keyboard-q/locales/fil.pak
/usr/lib/das-keyboard-q/locales/fr.pak
/usr/lib/das-keyboard-q/locales/gu.pak
/usr/lib/das-keyboard-q/locales/he.pak
/usr/lib/das-keyboard-q/locales/hi.pak
/usr/lib/das-keyboard-q/locales/hr.pak
/usr/lib/das-keyboard-q/locales/hu.pak
/usr/lib/das-keyboard-q/locales/id.pak
/usr/lib/das-keyboard-q/locales/it.pak
/usr/lib/das-keyboard-q/locales/ja.pak
/usr/lib/das-keyboard-q/locales/kn.pak
/usr/lib/das-keyboard-q/locales/ko.pak
/usr/lib/das-keyboard-q/locales/lt.pak
/usr/lib/das-keyboard-q/locales/lv.pak
/usr/lib/das-keyboard-q/locales/ml.pak
/usr/lib/das-keyboard-q/locales/mr.pak
/usr/lib/das-keyboard-q/locales/ms.pak
/usr/lib/das-keyboard-q/locales/nb.pak
/usr/lib/das-keyboard-q/locales/nl.pak
/usr/lib/das-keyboard-q/locales/pl.pak
/usr/lib/das-keyboard-q/locales/pt-BR.pak
/usr/lib/das-keyboard-q/locales/pt-PT.pak
/usr/lib/das-keyboard-q/locales/ro.pak
/usr/lib/das-keyboard-q/locales/ru.pak
/usr/lib/das-keyboard-q/locales/sk.pak
/usr/lib/das-keyboard-q/locales/sl.pak
/usr/lib/das-keyboard-q/locales/sr.pak
/usr/lib/das-keyboard-q/locales/sv.pak
/usr/lib/das-keyboard-q/locales/sw.pak
/usr/lib/das-keyboard-q/locales/ta.pak
/usr/lib/das-keyboard-q/locales/te.pak
/usr/lib/das-keyboard-q/locales/th.pak
/usr/lib/das-keyboard-q/locales/tr.pak
/usr/lib/das-keyboard-q/locales/uk.pak
/usr/lib/das-keyboard-q/locales/vi.pak
/usr/lib/das-keyboard-q/locales/zh-CN.pak
/usr/lib/das-keyboard-q/locales/zh-TW.pak
/usr/lib/das-keyboard-q/natives_blob.bin
/usr/lib/das-keyboard-q/resources
/usr/lib/das-keyboard-q/resources/app.asar
/usr/lib/das-keyboard-q/resources/app.asar.unpacked
/usr/lib/das-keyboard-q/resources/app.asar.unpacked/assets
/usr/lib/das-keyboard-q/resources/app.asar.unpacked/assets/externalLibraries
/usr/lib/das-keyboard-q/resources/app.asar.unpacked/assets/externalLibraries/DKWindowsUserServicesHelper.exe
/usr/lib/das-keyboard-q/resources/app.asar.unpacked/assets/externalLibraries/Das_Keyboard_User_Services.dll
/usr/lib/das-keyboard-q/resources/app.asar.unpacked/assets/externalLibraries/test.js
/usr/lib/das-keyboard-q/resources/app.asar.unpacked/assets/images
/usr/lib/das-keyboard-q/resources/app.asar.unpacked/assets/images/16x16.png
/usr/lib/das-keyboard-q/resources/app.asar.unpacked/assets/images/5Q-box-back.jpg
/usr/lib/das-keyboard-q/resources/app.asar.unpacked/assets/images/DK4QPID-home-icon.png
/usr/lib/das-keyboard-q/resources/app.asar.unpacked/assets/images/DK5QPID-home-icon.png
/usr/lib/das-keyboard-q/resources/app.asar.unpacked/assets/images/X50QPID-home-icon.png
/usr/lib/das-keyboard-q/resources/app.asar.unpacked/assets/images/bg.gif
/usr/lib/das-keyboard-q/resources/app.asar.unpacked/assets/images/dk5-q-blurry.png
/usr/lib/das-keyboard-q/resources/app.asar.unpacked/assets/images/gray-q-icon-no-bracket.png
/usr/lib/das-keyboard-q/resources/app.asar.unpacked/assets/images/gray-q-icon.png
/usr/lib/das-keyboard-q/resources/app.asar.unpacked/assets/images/icon.icns
/usr/lib/das-keyboard-q/resources/app.asar.unpacked/assets/images/ifttt
/usr/lib/das-keyboard-q/resources/app.asar.unpacked/assets/images/ifttt/DK4QPID.png
/usr/lib/das-keyboard-q/resources/app.asar.unpacked/assets/images/ifttt/DK5QPID.png
/usr/lib/das-keyboard-q/resources/app.asar.unpacked/assets/images/ifttt/X50QPID.png
/usr/lib/das-keyboard-q/resources/app.asar.unpacked/assets/images/layouts
/usr/lib/das-keyboard-q/resources/app.asar.unpacked/assets/images/layouts/5Q
/usr/lib/das-keyboard-q/resources/app.asar.unpacked/assets/images/layouts/5Q/5Q-da.png
/usr/lib/das-keyboard-q/resources/app.asar.unpacked/assets/images/layouts/5Q/5Q-de-DE.png
/usr/lib/das-keyboard-q/resources/app.asar.unpacked/assets/images/layouts/5Q/5Q-en-UK.png
/usr/lib/das-keyboard-q/resources/app.asar.unpacked/assets/images/layouts/5Q/5Q-en-US-MAC.png
/usr/lib/das-keyboard-q/resources/app.asar.unpacked/assets/images/layouts/5Q/5Q-en-US.png
/usr/lib/das-keyboard-q/resources/app.asar.unpacked/assets/images/layouts/5Q/5Q-es-ES.png
/usr/lib/das-keyboard-q/resources/app.asar.unpacked/assets/images/layouts/5Q/5Q-fr-FR.png
/usr/lib/das-keyboard-q/resources/app.asar.unpacked/assets/images/layouts/5Q/5Q-it-IT.png
/usr/lib/das-keyboard-q/resources/app.asar.unpacked/assets/images/layouts/5Q/5Q-ru.png
/usr/lib/das-keyboard-q/resources/app.asar.unpacked/assets/images/layouts/DK4Q
/usr/lib/das-keyboard-q/resources/app.asar.unpacked/assets/images/layouts/DK4Q/DK4Q-de-DE.png
/usr/lib/das-keyboard-q/resources/app.asar.unpacked/assets/images/layouts/DK4Q/DK4Q-en-UK.png
/usr/lib/das-keyboard-q/resources/app.asar.unpacked/assets/images/layouts/DK4Q/DK4Q-en-US-MAC.png
/usr/lib/das-keyboard-q/resources/app.asar.unpacked/assets/images/layouts/DK4Q/DK4Q-en-US.png
/usr/lib/das-keyboard-q/resources/app.asar.unpacked/assets/images/layouts/DK4Q/DK4Q-no.png
/usr/lib/das-keyboard-q/resources/app.asar.unpacked/assets/images/layouts/X50
/usr/lib/das-keyboard-q/resources/app.asar.unpacked/assets/images/layouts/X50-en-UK-drop.png
/usr/lib/das-keyboard-q/resources/app.asar.unpacked/assets/images/layouts/X50-en-UK.png
/usr/lib/das-keyboard-q/resources/app.asar.unpacked/assets/images/layouts/X50/X50-DEFAULT.png
/usr/lib/das-keyboard-q/resources/app.asar.unpacked/assets/images/layouts/X50/X50-da.png
/usr/lib/das-keyboard-q/resources/app.asar.unpacked/assets/images/layouts/X50/X50-de-DE.png
/usr/lib/das-keyboard-q/resources/app.asar.unpacked/assets/images/layouts/X50/X50-en-UK.png
/usr/lib/das-keyboard-q/resources/app.asar.unpacked/assets/images/layouts/X50/X50-en-US-MAC.png
/usr/lib/das-keyboard-q/resources/app.asar.unpacked/assets/images/layouts/X50/X50-en-US.png
/usr/lib/das-keyboard-q/resources/app.asar.unpacked/assets/images/layouts/X50/X50-es-ES.png
/usr/lib/das-keyboard-q/resources/app.asar.unpacked/assets/images/layouts/X50/X50-fr-FR.png
/usr/lib/das-keyboard-q/resources/app.asar.unpacked/assets/images/layouts/X50/X50-it-IT.png
/usr/lib/das-keyboard-q/resources/app.asar.unpacked/assets/images/layouts/X50/X50-ru.png
/usr/lib/das-keyboard-q/resources/app.asar.unpacked/assets/images/load.png
/usr/lib/das-keyboard-q/resources/app.asar.unpacked/assets/images/logo-big.png
/usr/lib/das-keyboard-q/resources/app.asar.unpacked/assets/images/logo.png
/usr/lib/das-keyboard-q/resources/app.asar.unpacked/assets/images/q-icon-no-bracket.png
/usr/lib/das-keyboard-q/resources/app.asar.unpacked/assets/images/q-icon.png
/usr/lib/das-keyboard-q/resources/app.asar.unpacked/assets/images/stars.png
/usr/lib/das-keyboard-q/resources/app.asar.unpacked/assets/scripts
/usr/lib/das-keyboard-q/resources/app.asar.unpacked/assets/scripts/launchMacDaemon.sh
/usr/lib/das-keyboard-q/resources/app.asar.unpacked/assets/scripts/linux.sh
/usr/lib/das-keyboard-q/resources/app.asar.unpacked/assets/scripts/mac.scpt
/usr/lib/das-keyboard-q/resources/app.asar.unpacked/assets/scripts/mac.sh
/usr/lib/das-keyboard-q/resources/app.asar.unpacked/assets/scripts/windows.ps1
/usr/lib/das-keyboard-q/resources/electron.asar
/usr/lib/das-keyboard-q/ui_resources_200_percent.pak
/usr/lib/das-keyboard-q/v8_context_snapshot.bin
/usr/lib/das-keyboard-q/version
/usr/lib/das-keyboard-q/views_resources_200_percent.pak
/usr/local/bin/das_keyboard_q-service
/usr/share/applications
/usr/share/applications/das-keyboard-q.desktop
/usr/share/doc
/usr/share/doc/das-keyboard-q
/usr/share/doc/das-keyboard-q/copyright
/usr/share/lintian
/usr/share/lintian/overrides
/usr/share/lintian/overrides/das-keyboard-q
/usr/share/pixmaps
/usr/share/pixmaps/das-keyboard-q.png

%changelog
