Summary:	IP Calculator
Name:		ipcalc
Version:	0.41
Release:	%mkrel 3
License:	GPLv2+
Group:		System/Servers
URL:		http://jodies.de/ipcalc
Source0:	http://jodies.de/ipcalc-archive/ipcalc-%{version}.tar.gz
Source1:	ipcalc_cgi.bz2
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
ipcalc takes an IP address and netmask and calculates the
resulting broadcast, network, Cisco wildcard mask, and host
range. By giving a second netmask, you can design sub- and
supernetworks. It is also intended to be a teaching tool and
presents the results as easy-to-understand binary values.

%prep

%setup -q

bzcat %{SOURCE1} > ipcalc.pl
perl -pi -e "s|/usr/local/bin|%{_bindir}|g" ipcalc.pl

%build

%install
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -d %{buildroot}/var/www/cgi-bin

install -m0755 ipcalc %{buildroot}%{_bindir}/
install -m0755 ipcalc.pl %{buildroot}/var/www/cgi-bin/

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc changelog license contributors
%attr(0755,root,root) %{_bindir}/ipcalc
%attr(0755,root,root) /var/www/cgi-bin/ipcalc.pl


