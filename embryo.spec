#Tarball of svn snapshot created as follows...
#Cut and paste in a shell after removing initial #

#svn co http://svn.enlightenment.org/svn/e/trunk/embryo embryo; \
#cd embryo; \
#SVNREV=$(LANGUAGE=C svn info | grep "Last Changed Rev:" | cut -d: -f 2 | sed "s@ @@"); \
#v_maj=$(cat configure.ac | grep 'm4_define(\[v_maj\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#v_min=$(cat configure.ac | grep 'm4_define(\[v_min\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#v_mic=$(cat configure.ac | grep 'm4_define(\[v_mic\],' | cut -d' ' -f 2 | cut -d[ -f 2 | cut -d] -f 1); \
#PKG_VERSION=$v_maj.$v_min.$v_mic.$SVNREV; \
#cd ..; \
#tar -Jcf embryo-$PKG_VERSION.tar.xz embryo/ --exclude .svn --exclude .*ignore

%define snapshot 0
%{?_snapshot: %{expand: %%global snapshot 1}}

%if %snapshot
%define	svndate	20120103
%define	svnrev	66150
%endif

%define	major 	1
%define	libname %mklibname %{name} %{major}
%define	develname %mklibname %{name} -d

Summary:	Enlightenment bytecode virtual machine
Name:		embryo
%if %snapshot
Version:	1.1.99.%{svnrev}
Release:	0.%{svndate}.1
%else
Version:	1.7.3
Release:	1
%endif
License:	BSD
Group:		Graphical desktop/Enlightenment
URL:		http://www.enlightenment.org/
%if %snapshot
Source0:	%{name}-%{version}.tar.xz
%else
Source0:	http://download.enlightenment.org/releases/%{name}-%{version}.tar.gz
%endif
BuildRequires:	pkgconfig(eina) >= 1.7.0

%description
Embryo is primarily a shared library that gives you an API to load and control
interpreted programs compiled into an abstract machine bytecode that it
understands.  This abstract (or virtual) machine is similar to a real machine
with a CPU, but it is emulated in software.

This package is part of the Enlightenment DR17 desktop shell.

%package -n %{libname}
Summary:	Libraries for the %{name} package
Group:		System/Libraries

%description -n %{libname}
Libraries for %{name}

%package -n %{develname}
Summary:	Headers and development libraries from %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
%{name} development headers and libraries.

%prep
%if %snapshot
%setup -qn %{name}
%else
%setup -q
%endif

%build
%if %snapshot
NOCONFIGURE=yes ./autogen.sh
%endif

%configure2_5x --disable-static
%make

%install
%makeinstall_std

%files
%doc AUTHORS COPYING README
%{_bindir}/%{name}_cc
%{_datadir}/%{name}

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%{_includedir}/%{name}*



%changelog
* Mon Jun 25 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.2.0-1
+ Revision: 806807
- version update 1.2.0

* Mon Jan 09 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.1.99.66150-0.20120103.1
+ Revision: 758816
- new snapshot/version 1.1.99.66150
- merged spec with UnityLinux
- cleaned up spec
- disabled static build

* Sat Jan 29 2011 Funda Wang <fwang@mandriva.org> 1.0.0-1
+ Revision: 633901
- 1.0.0 final

* Sat Dec 18 2010 Funda Wang <fwang@mandriva.org> 1.0.0-0.beta3.1mdv2011.0
+ Revision: 622797
- 1.0 beta3

* Tue Nov 16 2010 Funda Wang <fwang@mandriva.org> 1.0.0-0.beta2.1mdv2011.0
+ Revision: 597955
- 1.0.0 beta2

* Wed Oct 13 2010 Funda Wang <fwang@mandriva.org> 1.0.0-0.beta.1mdv2011.0
+ Revision: 585289
- 1.0.0 beta

* Sat Jul 10 2010 Funda Wang <fwang@mandriva.org> 0.9.9.49898-1mdv2011.0
+ Revision: 550185
- new verison 0.9.9.49898

* Sun Dec 13 2009 Funda Wang <fwang@mandriva.org> 0.9.9.063-1mdv2010.1
+ Revision: 478114
- new version 0.9.9.063

* Fri Aug 07 2009 Funda Wang <fwang@mandriva.org> 0.9.9.062-1mdv2010.0
+ Revision: 411058
- new version 0.9.9.062

* Mon Jul 06 2009 Funda Wang <fwang@mandriva.org> 0.9.9.061-1mdv2010.0
+ Revision: 392856
- fix file list
- new version 0.9.9.061
- protect major

* Sat May 02 2009 Funda Wang <fwang@mandriva.org> 0.9.9.060-1mdv2010.0
+ Revision: 370632
- New version 0.9.9.060

* Sat Feb 28 2009 Antoine Ginies <aginies@mandriva.com> 0.9.9.050-2mdv2009.1
+ Revision: 346218
- bump release
- SVN SNAPSHOT 20090227, release 0.9.9.050

* Sun Oct 12 2008 Funda Wang <fwang@mandriva.org> 0.9.9.050-1mdv2009.1
+ Revision: 292651
- new version 0.9.9.050

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 0.9.9.043-2mdv2009.0
+ Revision: 266619
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun Jun 01 2008 Funda Wang <fwang@mandriva.org> 0.9.9.043-1mdv2009.0
+ Revision: 213940
- New version 0.9.9.043

  + Antoine Ginies <aginies@mandriva.com>
    - bump release

* Fri Feb 15 2008 Antoine Ginies <aginies@mandriva.com> 0.9.1.042-2mdv2008.1
+ Revision: 168908
- bump release

* Sat Feb 02 2008 Austin Acton <austin@mandriva.org> 0.9.1.042-1mdv2008.1
+ Revision: 161504
- new version
- fix URL
- no major in devel package
- drop embryo-config

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Oct 31 2007 Antoine Ginies <aginies@mandriva.com> 0.9.1.041-2mdv2008.1
+ Revision: 104068
- CVS SNAPSHOT 20071031, release 0.9.1.041

* Thu Aug 30 2007 Antoine Ginies <aginies@mandriva.com> 0.9.1.041-1mdv2008.0
+ Revision: 76314
- fix missing file embryo-config
- fix path in tarball
- CVS SNAPSHOT 20070830, release 0.9.1.041

* Tue May 29 2007 Antoine Ginies <aginies@mandriva.com> 0.9.1.038-3mdv2008.0
+ Revision: 32624
- CVS SNAPSHOT 20070529, release 0.9.1.038

* Thu May 24 2007 Antoine Ginies <aginies@mandriva.com> 0.9.1.038-2mdv2008.0
+ Revision: 30642
- increase mkrel
- CVS snapshot 20070524, release 0.9.1.038
- remove unwanted changelog

* Mon May 21 2007 Antoine Ginies <aginies@mandriva.com> 0.9.1.038-1mdv2008.0
+ Revision: 29185
- CVS snapshot, release 0.9.1.038

* Mon Apr 23 2007 Pascal Terjan <pterjan@mandriva.org> 0.9.1.037-1mdv2008.0
+ Revision: 17403
- New snapshot
- Add an empty line at the end to not break multiarch macro
- Import embryo

