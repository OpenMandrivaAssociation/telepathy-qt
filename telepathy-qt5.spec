%define _enable_debug_packages %{nil}
%define debug_package %{nil}

%define oname telepathy-qt

Summary:	qt5 client for telepathy
Name:		telepathy-qt5
Version:	0.9.6.1
Release:	1
Group:		System/Libraries
License:	GPLv2
URL:		http://telepathy.freedesktop.org
Source0:	http://telepathy.freedesktop.org/releases/%{oname}/%{oname}-%{version}.tar.gz
BuildRequires:  pkgconfig(farstream-0.2)
BuildRequires:  pkgconfig(telepathy-farstream)
BuildRequires:  pkgconfig(telepathy-glib)
BuildRequires:  pkgconfig(gstreamer-interfaces-0.10)
BuildRequires:  python
BuildRequires:  python-dbus
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  qt4-devel
BuildRequires:  qt4-assistant
BuildRequires:  libxml2-utils

%description
Qt5 libraries for use in Telepathy clients and connection managers

#--------------------------------------------------------------------

%define libtelepathy_qt5_farstream_major 2
%define libtelepathy_qt5_farstream %mklibname telepathy-qt5-farstream %{libtelepathy_qt5_farstream_major}

%package -n %{libtelepathy_qt5_farstream}
Summary:        Core Decibel library
Group:          System/Libraries

%description -n %{libtelepathy_qt5_farstream}
Core Decibel library.

%files -n %{libtelepathy_qt5_farstream}
%{_libdir}/libtelepathy-qt5-farstream.so.%{libtelepathy_qt5_farstream_major}*

#--------------------------------------------------------------------

%define libtelepathy_qt5_major 2
%define libtelepathy_qt5 %mklibname telepathy-qt5_ %{libtelepathy_qt5_major}

%package -n %{libtelepathy_qt5}
Summary:        Core Decibel library
Group:          System/Libraries

%description -n %{libtelepathy_qt5}
Core Decibel library.

%files -n %{libtelepathy_qt5}
%{_libdir}/libtelepathy-qt5.so.%{libtelepathy_qt5_major}*

#--------------------------------------------------------------------

