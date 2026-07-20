%global kf_version 6.24.0

Name: kf6-kbookmarks
Version: 6.24.0
Release: 1%{?dist}
Summary: KDE Frameworks 6 Tier 3 addon for bookmarks manipulation
License: CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-3.0-only AND LicenseRef-KDE-Accepted-LGPL
URL:     https://invent.kde.org/frameworks/kbookmarks
Source0: %{name}-%{version}.tar.bz2

BuildRequires: kf6-extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: kf6-rpm-macros
BuildRequires: kf6-kcodecs-devel >= %{kf_version}
BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-qttools-devel

BuildRequires: kf6-kconfig-devel >= %{kf_version}
BuildRequires: kf6-kconfigwidgets-devel >= %{kf_version}
BuildRequires: kf6-kcolorscheme-devel >= %{kf_version}
BuildRequires: kf6-kcoreaddons-devel >= %{kf_version}
BuildRequires: kf6-kwidgetsaddons-devel >= %{kf_version}
BuildRequires: kf6-kxmlgui-devel >= %{kf_version}

%description
KBookmarks lets you access and manipulate bookmarks stored using the
XBEL format.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel
Requires:       kf6-kwidgetsaddons-devel
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

%files -f kbookmarks6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/kbookmarks.*
%{_kf6_datadir}/qlogging-categories6/kbookmarkswidgets.*
%{_kf6_libdir}/libKF6Bookmarks.so.*
%{_kf6_libdir}/libKF6BookmarksWidgets.so.*

%files devel
%{_kf6_includedir}/KBookmarks/
%{_kf6_libdir}/libKF6Bookmarks.so
%{_kf6_libdir}/cmake/KF6Bookmarks/
%{_kf6_includedir}/KBookmarksWidgets/
%{_kf6_libdir}/libKF6BookmarksWidgets.so

