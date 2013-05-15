%define	major	1
%define	libname %mklibname %{name} %{major}
%define	devname %mklibname %{name} -d

Summary:	Enlightenment bytecode virtual machine
Name:		embryo
Version:	1.7.7
Release:	1
License:	BSD
Group:		Graphical desktop/Enlightenment
URL:		http://www.enlightenment.org/
Source0:	http://download.enlightenment.fr/releases/%{name}-%{version}.tar.bz2
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

%package -n %{devname}
Summary:	Headers and development libraries from %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
%{name} development headers and libraries.

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%files
%doc AUTHORS COPYING README
%{_bindir}/%{name}_cc
%{_datadir}/%{name}

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}*

%files -n %{devname}
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%{_includedir}/%{name}*

