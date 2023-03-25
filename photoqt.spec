Name:		photoqt
Version:	3.1
Release:	1
Summary:	Image viewer
License:	GPLv3
Group:		Graphics
URL:		http://photoqt.org/
Source0:	http://photoqt.org/pkgs/%{name}-%{version}.tar.gz

BuildRequires:	desktop-file-utils
BuildRequires:	qmake5
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt5Concurrent)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	pkgconfig(Qt5QuickControls2)
BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Multimedia)
BuildRequires:	pkgconfig(Qt5Sql)
BuildRequires:	pkgconfig(Qt5Xml)
BuildRequires:	pkgconfig(Qt5PrintSupport)
BuildRequires:	pkgconfig(GraphicsMagick)
BuildRequires:	pkgconfig(exiv2)
BuildRequires:	pkgconfig(libraw)
BuildRequires:	pkgconfig(poppler-qt5)
BuildRequires:	pkgconfig(pugixml)
BuildRequires:	pkgconfig(IL)
BuildRequires:	pkgconfig(libarchive)
BuildRequires:	pkgconfig(python)
BuildRequires:	python3dist(pip)
#BuildRequires:	freeimage-devel
#BuildRequires:  freeimage3
BuildRequires:	qt5-linguist-tools
BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig(phonon4qt5)
BuildRequires:	qt5-qtimageformats-devel

Requires:	qt5-database-plugin-sqlite
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

%build
%cmake_qt5 -DFREEIMAGE=OFF -DCHROMECAST=OFF
%make_build

%install
%make_install -C build

mkdir -p %{buildroot}%{_datadir}/%{name}/lang
cp -r build/*.qm %{buildroot}%{_datadir}/%{name}/lang/

%find_lang %{name} --with-qt --all-name
