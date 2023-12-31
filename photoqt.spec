Name:		photoqt
Version:	4.1
Release:	1
Summary:	Image viewer
License:	GPLv3
Group:		Graphics
URL:		http://photoqt.org/
Source0:	http://photoqt.org/pkgs/%{name}-%{version}.tar.gz

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
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  pkgconfig(poppler-qt6)
BuildRequires:	pkgconfig(GraphicsMagick)
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
BuildRequires:	pkgconfig(phonon4qt5)

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
%cmake -DFREEIMAGE=OFF -DCHROMECAST=OFF -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

mkdir -p %{buildroot}%{_datadir}/%{name}/lang
cp -r build/*.qm %{buildroot}%{_datadir}/%{name}/lang/

%find_lang %{name} --with-qt --all-name
