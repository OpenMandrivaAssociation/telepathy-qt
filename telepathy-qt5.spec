%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	qt5 client for telepathy
Name:		telepathy-qt
Version:	0.9.6
Release:	1
Group:		System/Libraries
License:	GPLv2
URL:		http://telepathy.freedesktop.org
Source0:	http://telepathy.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	doxygen
BuildRequires:  pkgconfig(telepathy-glib)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:	pkgconfig(farstream-0.2)
BuildRequires:	pkgconfig(telepathy-farstream)
BuildRequires:	pkgconfig(gstreamer-1.0)
BuildRequires:	cmake(ECM)
BuildRequires:  libxml2-utils
BuildRequires:  cmake(Qt5Core)
BuildRequires:	cmake*Qt5Help)
BuildRequires:  doxygen
BuildRequires:  libxml2-utils
BuildRequires:	Python
BuildRequires:	Python-dbus


%description
Library for QT5-based Telepathy Client.

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build


# WARNING
# each library needs to follow OpenMandriva library policy
%files
%doc README NEWS AUTHORS
%{_libdir}/libtelepathy-qt5.so.0.0.9.7
%{_libdir}/libtelepathy-qt5.so.0
%{_libdir}/libtelepathy-qt5.so
%{_libdir}/libtelepathy-qt5-service.a
%{_libdir}/libtelepathy-qt5-farstream.so.0.0.9.7
%{_libdir}/libtelepathy-qt5-farstream.so.0
%{_libdir}/libtelepathy-qt5-farstream.so

