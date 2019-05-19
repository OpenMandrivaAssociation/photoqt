Name:		photoqt
Version:	1.7.1
Release:	2
Summary:	Image viewer
License:	GPLv3
Group:		Graphics
URL:		http://photoqt.org/
Source0:	http://photoqt.org/pkgs/%{name}-%{version}.tar.gz
BuildRequires:	desktop-file-utils
BuildRequires:	qmake5
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Sql)
BuildRequires:	pkgconfig(Qt5Xml)
BuildRequires:	pkgconfig(GraphicsMagick)
BuildRequires:	pkgconfig(exiv2)
BuildRequires:	pkgconfig(libraw)
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(poppler-qt5)
BuildRequires:	pkgconfig(IL)
BuildRequires:	pkgconfig(libarchive)
BuildRequires:	freeimage-devel
#BuildRequires:  freeimage
BuildRequires:	qt5-linguist-tools
BuildRequires:	desktop-file-utils
BuildRequires:  pkgconfig(phonon4qt5)


Requires:	qt5-database-plugin-sqlite
Requires:	graphicsmagick

%description
Image viewer with a simple and fast interface, 
being good looking and highly configurable.

%files -f %{name}.lang
%doc CHANGELOG README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_datadir}/appdata/%{name}.appdata.xml
#---------------------------------------------------

%prep
%autosetup -p1
sed -i 's|Debug|Release|' CMakeLists.txt

%build
%cmake_qt5
%make_build

%install
%make_install
#
mkdir -p %{buildroot}%{_datadir}/%{name}/lang
cp -r build/*.qm %{buildroot}%{_datadir}/%{name}/lang/

%find_lang %{name} --with-qt --all-name
