%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	qt5 client for telepathy
Name:		telepathy-qt5
Version:	0.9.7
Release:	1
Epoch:		1
Group:		Plasma/Other
License:	GPLv2
URL:		git://anongit.freedesktop.org/telepathy/telepathy-qt4
BuildRequires:	pkgconfig(farstream-0.2)
BuildRequires:	pkgconfig(telepathy-farstream)
BuildRequires:	pkgconfig(telepathy-glib)
BuildRequires:	pkgconfig(gstreamer-1.0)
BuildRequires:	python
BuildRequires:	python-dbus
BuildRequires:	cmake
BuildRequires:	doxygen
BuildRequires:	libxml2-utils
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Help)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5Declarative)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	qml-material
BuildRequires:	intltool

%description
Library for QT5-based Telepathy CLient

%prep
%setup -q
%cmake_kde5

%build
%make
