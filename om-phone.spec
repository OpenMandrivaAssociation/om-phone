Name:		om-phone
Summary:	Phone dialer for Plasma Mobile
Version:	0.0.1
Release:	1
License:	GPLv3
Source0:	https://github.com/OpenMandrivaSoftware/om-phone/archive/%{version}/%{name}-%{version}.tar.gz
Requires:	modemmanager
BuildRequires:	%{_lib}phonenumber-devel
BuildRequires:	pkgconfig(protobuf)
BuildRequires:	pkgconfig(ModemManager)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	qmake5

%description
Phone dialer for Plasma Mobile

%prep
%autosetup -p1
%cmake \
	-DUSE_LIBPHONENUMBER:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_sysconfdir}/xdg/autostart/ch.lindev.phone.autostart.desktop
%{_bindir}/phone
%{_datadir}/applications/ch.lindev.phone.desktop
%{_datadir}/icons/hicolor/scalable/apps/ch.lindev.phone.svg
