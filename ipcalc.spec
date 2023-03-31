Summary:	IP network address calculator
Name:		ipcalc
Version:	1.0.1
Release:	2
Group:		System/Base
License:	GPLv2+
URL:		https://gitlab.com/ipcalc/ipcalc
Source0:	https://gitlab.com/ipcalc/ipcalc/-/archive/%{version}//%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(geoip)
BuildRequires:	pkgconfig(popt)
BuildRequires:	ronn
Conflicts:	initscripts < 9.64

%description
ipcalc provides a simple way to calculate IP information for a host
or network. Depending on the options specified, it may be used to provide
IP network information in human readable format, in a format suitable for
parsing in scripts, generate random private addresses, resolve an IP address,
or check the validity of an address.

%prep
%autosetup -p1

%build
%set_build_flags
%make_build LIBPATH=%{_libdir} USE_GEOIP="yes"

%install
mkdir -p %{buildroot}%{_bindir}
install -p -m 755 ipcalc %{buildroot}%{_bindir}/
mkdir -p -m 755 %{buildroot}%{_mandir}/man1
# Make sure we don't hit "invalid byte sequence in US-ASCII" in ronn
export LC_ALL=en_US.UTF-8
ronn --pipe -r ipcalc.1.md >ipcalc.1
install -p -m 644 ipcalc.1 %{buildroot}%{_mandir}/man1

%files
%doc README.md
%{_bindir}/ipcalc
%{_mandir}/man1/ipcalc.1*
