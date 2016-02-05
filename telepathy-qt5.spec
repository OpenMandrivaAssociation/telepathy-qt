%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	qt5 client for telepathy
Name:		telepathy-qt
Version:	0.9.6.1
Release:	1
Group:		System/Libraries
License:	GPLv2
Url:		http://telepathy.freedesktop.org/wiki
Source0:	http://telepathy.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(farstream-0.2)
BuildRequires:	pkgconfig(telepathy-farstream)
BuildRequires:	pkgconfig(telepathy-glib)
BuildRequires:	pkgconfig(gstreamer-1.0)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5Xml)
BuildRequires:	python
BuildRequires:	python-dbus
BuildRequires:	cmake
BuildRequires:	doxygen
BuildRequires:	libxml2-utils

%description
Qt5 libraries for use in Telepathy clients and connection managers

#--------------------------------------------------------------------

%define farstream_major 2
%define libfarstream %mklibname telepathy-qt5-farstream %{farstream_major}

%package -n %{libfarstream}
Summary:        Core Decibel library
Group:          System/Libraries

%description -n %{libfarstream}
Core Decibel library.

%files -n %{libfarstream}
%{_libdir}/libtelepathy-qt5-farstream.so.%{farstream_major}*

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


%prep
%setup -q

%build
%cmake_qt5
%make

%install
%makeinstall -C build
