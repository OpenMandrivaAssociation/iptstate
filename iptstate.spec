Summary:	Display IP Tables state table information in a "top"-like interface
Name:		iptstate
Version:	2.2.5
Release:	1
Group:		Monitoring
License:	zlib/libpng License
URL:		http://www.phildev.net/iptstate/
Source0:	http://www.phildev.net/iptstate/%{name}-%{version}.tar.bz2
Source1:	http://www.phildev.net/iptstate/%{name}-%{version}.tar.bz2.asc
BuildRequires:	ncurses-devel
BuildRequires:	gpm-devel
BuildRequires:	netfilter_conntrack-devel >= 0.0.50

%description
IP Tables State (iptstate) was originally written to impliment the "state top"
feature of IP Filter. "State top" displays the states held by your stateful
firewall in a "top"-like manner.

Since IP Tables doesn't have a built in way to easily display this information
even once, an option was added to just display the state table once and exit.

%prep
%setup -q

%build
%serverbuild
%make CXXFLAGS="$CFLAGS -Wall"
 
%install
%makeinstall PREFIX=%{buildroot}%{_prefix}

%files
%doc README BUGS Changelog LICENSE CONTRIB WISHLIST
%{_sbindir}/%{name}
%{_mandir}/man8/%{name}.8*


%changelog
* Sun Jun 03 2012 Oden Eriksson <oeriksson@mandriva.com> 2.2.5-1
+ Revision: 802115
- 2.2.5

* Mon Apr 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2.2.3-1
+ Revision: 650153
- 2.2.3

* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 2.2.2-3mdv2011.0
+ Revision: 612405
- the mass rebuild of 2010.1 packages

* Thu Apr 22 2010 Oden Eriksson <oeriksson@mandriva.com> 2.2.2-2mdv2010.1
+ Revision: 538001
- rebuilt against new libnetfilter_conntrack libs

* Mon Feb 15 2010 Sandro Cazzaniga <kharec@mandriva.org> 2.2.2-1mdv2010.1
+ Revision: 506082
- Update to 2.2.2
- Fix licence
- clean spec
- drop old patch

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 2.2.1-5mdv2010.0
+ Revision: 429537
- rebuild

* Sat Sep 20 2008 Oden Eriksson <oeriksson@mandriva.com> 2.2.1-4mdv2009.0
+ Revision: 286156
- added a gcc43 patch from gentoo

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Wed Oct 17 2007 Oden Eriksson <oeriksson@mandriva.com> 2.2.1-1mdv2008.1
+ Revision: 99758
- 2.2.1

* Mon Aug 20 2007 Thierry Vignaud <tv@mandriva.org> 1.4-1mdv2008.0
+ Revision: 67559
- use %%mkrel


* Sun Apr 17 2005 Oden Eriksson <oeriksson@mandriva.com> 1.4-1mdk
- 1.4
- drop the opt patch, it's not needed anymore

* Thu Jun 17 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.3-2mdk
- rebuild

* Wed Jan 14 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.3-1mdk
- 1.3

* Sat Aug 30 2003 Marcel Pol <mpol@gmx.net> 1.2.1-1mdk
- 1.2.1
- drop patch0, merged upstream
- rediff patch1
- new url

* Thu Jan 30 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.2.0-5mdk
- rebuild

* Mon Jan 20 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 1.2.0-4mdk
- build release
- misc spec file fixes

* Thu Sep 05 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.2.0-3mdk
- rebuild

* Tue May 28 2002 Oden Eriksson <oden.eriksson@kvikkjokk.net> 1.2.0-2mdk
- rebuilt with gcc3.1
- added P0 from the author as a temporary fix.
- added P1 to utilize %%optflags
- misc spec file fixes

* Wed Apr 24 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.2.0-1mdk
- updated by Garrick Staples <garrick@speculation.org>

