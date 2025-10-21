%global kf6_version 6.18.0

Name: kf6-kbookmarks
Version: 6.18.0
Release: 1%{?dist}
Summary: KDE Frameworks 6 Tier 3 addon for bookmarks manipulation

License: LGPLv2+
URL:     https://invent.kde.org/frameworks/kbookmarks
Source0: %{name}-%{version}.tar.bz2

BuildRequires: kf6-extra-cmake-modules
BuildRequires: kf6-rpm-macros
BuildRequires: kf6-kcodecs-devel >= %{kf6_version}
BuildRequires: kf6-kconfig-devel >= %{kf6_version}
BuildRequires: kf6-kconfigwidgets-devel >= %{kf6_version}
BuildRequires: kf6-kcoreaddons-devel >= %{kf6_version}
BuildRequires: kf6-kwidgetsaddons-devel >= %{kf6_version}
BuildRequires: kf6-kxmlgui-devel >= %{kf6_version}

BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-qttools-devel

%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
Requires: qt6-qtbase-gui
Requires: kf6-kcodecs >= %{kf6_version}
Requires: kf6-kconfig >= %{kf6_version}
Requires: kf6-kconfigwidgets >= %{kf6_version}
Requires: kf6-kcoreaddons >= %{kf6_version}
Requires: kf6-kwidgetsaddons >= %{kf6_version}

%description
KBookmarks lets you access and manipulate bookmarks stored using the
XBEL format.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires: qt6-qtbase-devel
Requires: kf6-kwidgetsaddons-devel >= %{kf6_version}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{version}/upstream -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%find_lang_kf6 kbookmarks6_qt


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/kbookmarks.*
%{_kf6_libdir}/libKF6Bookmarks.so.*
%{_kf6_datadir}/locale/

%files devel

%{_kf6_includedir}/KF6/KBookmarks/
%{_kf6_libdir}/libKF6Bookmarks.so
%{_kf6_libdir}/cmake/KF6Bookmarks/
%{_kf6_archdatadir}/mkspecs/modules/qt_KBookmarks.pri

