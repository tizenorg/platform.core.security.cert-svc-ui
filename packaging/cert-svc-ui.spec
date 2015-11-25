Name:    cert-svc-ui
Summary: Certification service ui package
Version: 1.0.1
Release: 53
Group:   System/Libraries
License: Apache-2.0
Source0: %{name}-%{version}.tar.gz
Source1001: %{name}.manifest
%if "%{?tizen_profile_name}" == "tv"
ExcludeArch: %{arm} %ix86 x86_64
%endif
BuildRequires: cmake
BuildRequires: gettext-tools
BuildRequires: edje-tools
BuildRequires: pkgconfig(dlog)
BuildRequires: pkgconfig(cert-svc-vcore)
BuildRequires: pkgconfig(edje)
BuildRequires: pkgconfig(eina)
BuildRequires: pkgconfig(elementary)
BuildRequires: pkgconfig(evas)
BuildRequires: pkgconfig(efl-extension)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(ui-gadget-1)
BuildRequires: pkgconfig(icu-i18n)
BuildRequires: pkgconfig(vconf)
BuildRequires: pkgconfig(capi-system-system-settings)
BuildRequires: pkgconfig(libtzplatform-config)
Requires: pkgconfig(libtzplatform-config)

%description
Certification service ui package, used by settings and ui-gadget

%prep
%setup -q
cp -a %{SOURCE1001} .

%build
export CFLAGS="$CFLAGS -DTIZEN_DEBUG_ENABLE"
export CXXFLAGS="$CXXFLAGS -DTIZEN_DEBUG_ENABLE"
export FFLAGS="$FFLAGS -DTIZEN_DEBUG_ENABLE"

export CFLAGS="$CFLAGS -DTIZEN_ENGINEER_MODE"
export CXXFLAGS="$CXXFLAGS -DTIZEN_ENGINEER_MODE"
export FFLAGS="$FFLAGS -DTIZEN_ENGINEER_MODE"

%ifarch %{ix86}
export CFLAGS="$CFLAGS -DTIZEN_EMULATOR_MODE"
export CXXFLAGS="$CXXFLAGS -DTIZEN_EMULATOR_MODE"
export FFLAGS="$FFLAGS -DTIZEN_EMULATOR_MODE"
%endif

%{!?build_type:%define build_type "Release"}
cmake . -DCMAKE_INSTALL_PREFIX=%TZ_SYS_RO_UG \
        -DTZ_SYS_BIN=%{TZ_SYS_BIN} \
        -DTZ_SYS_SHARE=%{TZ_SYS_SHARE} \
        -DCMAKE_BUILD_TYPE=%{build_type}

#VERBOSE=1 make
make

%install
%make_install

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%manifest %{name}.manifest
%license LICENSE
%{TZ_SYS_SHARE}/packages/%{name}.xml
%TZ_SYS_RO_UG/lib/libug-mgr-cert-view.so*
%TZ_SYS_RO_UG/lib/libug-setting-manage-certificates-efl.so*
%TZ_SYS_RO_UG/lib/libug-cert-selection-ug-efl.so*
%TZ_SYS_RO_UG/res/locale/*/LC_MESSAGES/*
%TZ_SYS_RO_UG/res/images
%TZ_SYS_RO_UG/res/custom_editfield.edj
