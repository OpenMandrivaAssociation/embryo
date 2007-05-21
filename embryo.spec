%define	name	embryo
%define	version 0.9.1.038
%define release %mkrel 1

%define major 	0
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} %major -d

Summary: 	Enlightenment bytecode virtual machine
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	BSD
Group: 		Graphical desktop/Enlightenment
URL: 		http://get-e.org/
Source: 	%{name}-%{version}.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires:	multiarch-utils

%description
Embryo is primarily a shared library that gives you an API to load and control
interpreted programs compiled into an abstract machine bytecode that it
understands.  This abstract (or virtual) machine is similar to a real machine
with a CPU, but it is emulated in software.

This package is part of the Enlightenment DR17 desktop shell.

%package -n %libname
Summary: Libraries for the %{name} package
Group: System/Libraries
Provides: %libname = %{version}-%{release}

%description -n %libname
Libraries for %{name}

%package -n %libnamedev
Summary: Headers and development libraries from %{name}
Group: Development/Other
Requires: %libname = %{version}
Provides: lib%{name}-devel = %{version}-%{release}
Provides: %name-devel = %{version}-%{release}

%description -n %libnamedev
%{name} development headers and libraries

%prep
%setup -q 

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
%multiarch_binaries %buildroot/%_bindir/%name-config

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README
%{_bindir}/%{name}_cc
%{_datadir}/%name

%files -n %libname
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %libnamedev
%defattr(-,root,root)
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_includedir}/*.h
%{_bindir}/%name-config
%multiarch %multiarch_bindir/%name-config



%changelog
* Wed May 16 2007 Antoine Ginies <aginies@mandriva.com> 0.9.1.038-1mdv2008.0
- cvs snapshot 20070516

* Mon Apr 23 2007 Pascal Terjan <pterjan@mandriva.org> 0.9.1.037-1mdv2008.0
+ Revision: 17403
- New snapshot
- Add an empty line at the end to not break multiarch macro
- Import embryo



* Fri Mar 24 2006 Austin Acton <austin@mandriva.org> 0.9.1.025-0.20060323.1mdk
- new cvs checkout

* Fri Feb 17 2006 Austin Acton <austin@mandriva.org> 0.9.1.023-0.20060216.1mdk
- new cvs checkout

* Wed Jan 18 2006 Austin Acton <austin@mandriva.org> 0.9.1.023-0.20060117.1mdk
- new cvs checkout

* Thu Jan 12 2006 Austin Acton <austin@mandriva.org> 0.9.1.022-0.20060111.1mdk
- new cvs checkout

* Fri Nov 25 2005 Austin Acton <austin@mandriva.org> 0.9.1.019-0.20051124.1mdk
- new cvs checkout

* Wed Nov 09 2005 Austin Acton <austin@mandriva.org> 0.9.1.018-0.20051109.1mdk
- new cvs checkout

* Sat Nov 05 2005 Austin Acton <austin@mandriva.org> 0.9.1.018-0.20051104.1mdk
- new cvs checkout

* Mon Sep 05 2005 Austin Acton <austin@mandriva.org> 0.9.1.013-0.20050904.1mdk
- new cvs checkout

* Sun Aug 14 2005 Austin Acton <austin@mandriva.org> 0.9.1.013-0.20050813.1mdk
- new cvs checkout

* Mon Jun 27 2005 Austin Acton <austin@mandriva.org> 0.9.1.010-0.20050627.1mdk
- new cvs checkout

* Wed Jun 08 2005 Austin Acton <austin@mandriva.org> 0.9.1.008-0.20050608.1mdk
- new cvs checkout

* Wed May 25 2005 Austin Acton <austin@mandriva.org> 0.9.1.007-0.20050524.2mdk
- multiarch binaries

* Wed May 25 2005 Austin Acton <austin@mandriva.org> 0.9.1.007-0.20050524.1mdk
- new cvs checkout

* Sun May 15 2005 Austin Acton <ausitn@mandriva.org> 0.9.1.007-0.20050511.2mdk
- clean spec

* Thu May 12 2005 Austin Acton <austin@mandriva.org> 0.9.1.007-0.20050511.1mdk
- use cvs version 0.9.1.025
- use my spec file

* Fri Sep 24 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.0.1-0.20040913.1mdk
- 0.0.1 20040913
