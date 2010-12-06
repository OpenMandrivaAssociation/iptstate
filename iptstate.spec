Summary:	Display IP Tables state table information in a "top"-like interface
Name:		iptstate
Version:	2.2.2
Release:	%mkrel 3
Group:		Monitoring
License:	zlib/libpng License
URL:		http://www.phildev.net/iptstate/
Source0:	http://www.phildev.net/iptstate/%{name}-%{version}.tar.bz2
Source1:	http://www.phildev.net/iptstate/%{name}-%{version}.tar.bz2.asc
BuildRequires:	ncurses-devel
BuildRequires:	gpm-devel 
BuildRequires:	libnetfilter_conntrack-devel >= 0.0.50
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
rm -rf %{buildroot}
%makeinstall PREFIX=%{buildroot}%{_prefix}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc README BUGS Changelog LICENSE CONTRIB WISHLIST
%{_sbindir}/%{name}
%{_mandir}/man8/%{name}.8*
