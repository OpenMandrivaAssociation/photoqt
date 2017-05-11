Name:		photoqt
Version:	1.5.1
Release:	1
Summary:	Image viewer
License:	GPLv3
Group:		Graphics
URL:		http://photoqt.org/
Source0:	http://photoqt.org/pkgs/%{name}-%{version}.tar.gz
BuildRequires:	desktop-file-utils
BuildRequires:	qt5-devel
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:	pkgconfig(GraphicsMagick)
BuildRequires:	pkgconfig(exiv2)
BuildRequires:	pkgconfig(libraw)
BuildRequires:	phonon-devel
BuildRequires:	cmake
BuildRequires:	qt5-linguist-tools
BuildRequires:	desktop-file-utils
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
%setup -q
sed -i 's|Debug|Release|' CMakeLists.txt

%build
%cmake_qt5
%make

%install
%makeinstall_std -C build
#
mkdir -p %{buildroot}%{_datadir}/%{name}/lang
cp -r build/*.qm %{buildroot}%{_datadir}/%{name}/lang/

%find_lang %{name} --with-qt --all-name
