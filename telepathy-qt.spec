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
Patch0:		telepathy-qt-0.9.4-fix-link.patch
Patch1:		0.9.6.1-default-source.patch
Patch2:		0.9.6.1-yes-release.patch
Patch3:		telepathy-qt-0.9.6.1-gstreamer-1.5.patch
BuildRequires:	pkgconfig(telepathy-farstream) >= 0.6
BuildRequires:	pkgconfig(telepathy-glib)
BuildRequires:	pkgconfig(farstream-0.2)
BuildRequires:	pkgconfig(gstreamer-1.0)
BuildRequires:	pkgconfig(QtCore)
BuildRequires:	pkgconfig(Qt5Concurrent)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	pkgconfig(Qt5QuickWidgets)
BuildRequires:	pkgconfig(Qt5Script)
BuildRequires:	pkgconfig(Qt5Sql)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5WebKit)
BuildRequires:	pkgconfig(Qt5WebKitWidgets)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5X11Extras)
BuildRequires:	pkgconfig(Qt5Xml)
BuildRequires:	python2
BuildRequires:	python-dbus
BuildRequires:	cmake
BuildRequires:	doxygen
BuildRequires:	libxml2-utils

%description
Qt5 libraries for use in Telepathy clients and connection managers.

#--------------------------------------------------------------------

%define farstream_major 0
%define libfarstream %mklibname telepathy-qt5-farstream %{farstream_major}

%package -n %{libfarstream}
Summary:        Core Decibel library
Group:          System/Libraries

%description -n %{libfarstream}
Core Decibel library.

%files -n %{libfarstream}
%{_libdir}/libtelepathy-qt5-farstream.so.%{farstream_major}*

#--------------------------------------------------------------------

%define libtelepathy_qt5_major 0
%define libtelepathy_qt5 %mklibname telepathy-qt5_ %{libtelepathy_qt5_major}

%package -n %{libtelepathy_qt5}
Summary:        Core Decibel library
Group:          System/Libraries

%description -n %{libtelepathy_qt5}
Core Decibel library.

%files -n %{libtelepathy_qt5}
%{_libdir}/libtelepathy-qt5.so.%{libtelepathy_qt5_major}*

#--------------------------------------------------------------------

%define develname %mklibname telepathy-qt5 -d

%package -n %{develname}
Summary:	%{name} development files
Group:		Development/KDE and Qt
Requires:	%{libtelepathy_qt5} = %{EVRD}
Requires:	%{libfarstream} = %{EVRD}

%description -n %{develname}
Telepathy Qt development files.

%files -n %{develname}
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%{_libdir}/libtelepathy-qt5-service.a
%{_libdir}/cmake/TelepathyQt5
%{_libdir}/cmake/TelepathyQt5Farstream/
%{_libdir}/cmake/TelepathyQt5Service/

#--------------------------------------------------------------------

%prep
%setup -q
%apply_patches

%build
export PYTHON=%{__python2}
%cmake_qt5 -DDESIRED_QT_VERSION=5 -DENABLE_EXAMPLES=OFF -DPYTHON_EXECUTABLE=%{__python2} -DENABLE_TESTS=OFF
PYTHON=%{__python2} %make

%install
%makeinstall DESTDIR=%{buildroot} -C build
