Summary:	IP network address calculator
Name:		ipcalc
Version:	0.1.6
Release:	1
License:	GPLv2+
URL:		https://github.com/nmav/ipcalc
Source0:	https://github.com/nmav/ipcalc/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(geoip)
BuildRequires:	pkgconfig(popt)
Conflicts:	initscripts < 9.64


%description
ipcalc provides a simple way to calculate IP information for a host
or network. Depending on the options specified, it may be used to provide
IP network information in human readable format, in a format suitable for
parsing in scripts, generate random private addresses, resolve an IP address,
or check the validity of an address.

%prep
%setup -q
%apply_patches

%build
%setup_compile_flags
%make LIBPATH=%{_libdir}

%install
mkdir -p %{buildroot}/bin
install -p -m 755 ipcalc %{buildroot}/bin/
mkdir -p -m 755 %{buildroot}%{_mandir}/man1
install -p -m 644 ipcalc.1 %{buildroot}%{_mandir}/man1

%files
%doc README.md COPYING
/bin/ipcalc
%{_mandir}/man1/ipcalc.1*
