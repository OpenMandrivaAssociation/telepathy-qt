%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	qt5 client for telepathy
Name:		telepathy-qt5
Version:	0.9.7
Release:	1
Epoch:		1
Group:		Plasma/Other
License:	GPLv2
BuildRequires:  python
BuildRequires:  python-dbus
BuildRequires:  doxygen
BuildRequires:  libxml2-utils
BuildRequires:  qml-material
BuildRequires:  intltool
BuildRequires:	pkgconfig(farstream-0.2)
BuildRequires:	pkgconfig(telepathy-farstream)
BuildRequires:	pkgconfig(telepathy-glib)
BuildRequires:	pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfie(Qt5Help)
BuildRequires:  cmake(ECM)
BuildRequires:  cmake(Kf5Declarative)
BuildRequires:  cmake(Kf5I18n)

%description
Library for QT5-based Telepathy CLient

%prep
%setup -q
%cmake_kde5

%build
%make
