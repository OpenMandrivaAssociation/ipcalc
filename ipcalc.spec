Summary:	IP Calculator
Name:		ipcalc
Version:	0.41
Release:	6
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




%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.41-5mdv2011.0
+ Revision: 619677
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.41-4mdv2010.0
+ Revision: 429517
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.41-3mdv2009.0
+ Revision: 247247
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Dec 18 2007 Nicolas Vigier <nvigier@mandriva.com> 0.41-1mdv2008.1
+ Revision: 132424
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Feb 02 2007 Oden Eriksson <oeriksson@mandriva.com> 0.40-1mdv2007.0
+ Revision: 115943
- Import ipcalc

* Sun Dec 25 2005 Oden Eriksson <oeriksson@mandriva.com> 0.38-2mdk
- rebuild

* Fri Oct 29 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.38-1mdk
- initial mandrake package

