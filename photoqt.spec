Name:		photoqt
Version:	4.5
Release:	2
Summary:	Image viewer
License:	GPLv3
Group:		Graphics
URL:		https://photoqt.org/
Source0:	https://photoqt.org/pkgs/%{name}-%{version}.tar.gz

BuildRequires:  gettext
BuildRequires:	desktop-file-utils
BuildRequires:	cmake(Qt6)
BuildRequires:	qmake-qt6
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:	cmake(Qt6QICNSPlugin)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6QmlCore)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  qt6-qtbase-sql-firebird
BuildRequires:  qt6-qtbase-sql-mariadb
BuildRequires:  qt6-qtbase-sql-odbc
BuildRequires:  qt6-qtbase-sql-postgresql
BuildRequires:  qt6-qtmultimedia-gstreamer
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  qml(QtNetwork)
BuildRequires:	qt6-qtbase-theme-gtk3
BuildRequires:  pkgconfig(poppler-qt6)
BuildRequires:	pkgconfig(GraphicsMagick)
BuildRequires:  pkgconfig(ImageMagick)
BuildRequires:	pkgconfig(exiv2)
BuildRequires:	pkgconfig(libraw)
BuildRequires:	pkgconfig(pugixml)
BuildRequires:	pkgconfig(IL)
BuildRequires:	pkgconfig(libarchive)
BuildRequires:	pkgconfig(python)
BuildRequires:	python3dist(pip)
#BuildRequires:	freeimage-devel
#BuildRequires:  freeimage3
BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig(phonon4qt6)
BuildRequires:  pkgconfig(mpv)
BuildRequires:  pkgconfig(zxing)

Requires:	qt6-qtbase-sql-sqlite
Requires:	graphicsmagick

%description
Image viewer with a simple and fast interface, 
being good looking and highly configurable.

%files -f %{name}.lang
%doc CHANGELOG README
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/*/apps/*.png
%{_metainfodir}/*.metainfo.xml

#---------------------------------------------------

%prep
%autosetup -p1
sed -i 's|Debug|Release|' CMakeLists.txt
%cmake -DFREEIMAGE=OFF -DCHROMECAST=OFF -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

mkdir -p %{buildroot}%{_datadir}/%{name}/lang
cp -r build/*.qm %{buildroot}%{_datadir}/%{name}/lang/

%find_lang %{name} --with-qt --all-name
