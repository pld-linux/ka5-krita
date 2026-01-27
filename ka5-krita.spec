# TODO:
# - KSeExpr 4.0.0.0 https://invent.kde.org/graphics/kseexpr
# - system raqm (bundled, modified? version is used)
%define		_state		stable
%define		qt_ver		5.12.0
%define		kf_ver		5.44.0
%define		orgname		krita

Summary:	A digital painting application
Summary(pl.UTF-8):	Aplikacja do rysunków cyfrowych
Name:		ka5-krita
Version:	5.2.15
Release:	1
License:	GPL v3+
Group:		X11/Applications/Graphics
Source0:	https://download.kde.org/%{_state}/krita/%{version}/%{orgname}-%{version}.tar.xz
# Source0-md5:	d4025582226c60f0c6c84d7c451f992b
# keep in sync with required sip6 version
Patch0:		krita-sip.patch
URL:		https://www.krita.org/
BuildRequires:	OpenColorIO-devel >= 1.1.1
BuildRequires:	OpenEXR-devel
BuildRequires:	Qt5Concurrent-devel >= %{qt_ver}
BuildRequires:	Qt5Core-devel >= %{qt_ver}
BuildRequires:	Qt5DBus-devel >= %{qt_ver}
BuildRequires:	Qt5Gui-devel >= %{qt_ver}
BuildRequires:	Qt5Network-devel >= %{qt_ver}
BuildRequires:	Qt5PrintSupport-devel >= %{qt_ver}
BuildRequires:	Qt5Qml-devel >= %{qt_ver}
BuildRequires:	Qt5Quick-devel >= %{qt_ver}
BuildRequires:	Qt5Sql-devel >= %{qt_ver}
BuildRequires:	Qt5Svg-devel >= %{qt_ver}
BuildRequires:	Qt5Test-devel >= %{qt_ver}
BuildRequires:	Qt5Widgets-devel >= %{qt_ver}
BuildRequires:	Qt5X11Extras-devel >= %{qt_ver}
BuildRequires:	Qt5Xml-devel >= %{qt_ver}
BuildRequires:	SDL2-devel >= 2.0
BuildRequires:	boost-devel >= 1.65
BuildRequires:	cmake >= 3.16
BuildRequires:	eigen3 >= 3.3
BuildRequires:	exiv2-devel >= 0.16
BuildRequires:	fftw3-devel >= 3
BuildRequires:	fontconfig-devel >= 2.13.1
BuildRequires:	freetype-devel >= 1:2.10.0
BuildRequires:	fribidi-devel >= 1.0.6
BuildRequires:	gettext-devel
BuildRequires:	giflib-devel
BuildRequires:	gsl-devel
BuildRequires:	harfbuzz-devel >= 4.0.0
BuildRequires:	immer-devel
BuildRequires:	ka5-libkdcraw-devel >= 5.0.0
BuildRequires:	kf5-extra-cmake-modules >= 5.22
BuildRequires:	kf5-kcompletion-devel >= %{kf_ver}
BuildRequires:	kf5-kconfig-devel >= %{kf_ver}
BuildRequires:	kf5-kcoreaddons-devel >= %{kf_ver}
BuildRequires:	kf5-kcrash-devel >= %{kf_ver}
BuildRequires:	kf5-kguiaddons-devel >= %{kf_ver}
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-kitemmodels-devel >= %{kf_ver}
BuildRequires:	kf5-kitemviews-devel >= %{kf_ver}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kf_ver}
BuildRequires:	kf5-kwindowsystem-devel >= %{kf_ver}
BuildRequires:	lager-devel
BuildRequires:	lcms2-devel >= 2.4
BuildRequires:	libheif-devel >= 1.11.0
BuildRequires:	libjpeg-turbo-devel >= 2.1.3
BuildRequires:	libjxl-devel >= 0.9.0
BuildRequires:	libmypaint-devel >= 1.4.0
BuildRequires:	libpng-devel >= 1.2.6
BuildRequires:	libquadmath-devel
BuildRequires:	libraw-devel >= 0.16
BuildRequires:	libstdc++-devel >= 6:7
BuildRequires:	libtiff-devel
BuildRequires:	libunibreak-devel >= 5.0
BuildRequires:	libwebp-devel >= 1.2.0
BuildRequires:	mlt-devel >= 7
BuildRequires:	ninja
BuildRequires:	openjpeg2-devel >= 2.3.0
BuildRequires:	pkgconfig
BuildRequires:	poppler-qt5-devel
BuildRequires:	python3-PyQt5 >= 5.6.0
BuildRequires:	python3-PyQt5-devel >= 4.19.13
BuildRequires:	python3-devel >= 1:3.8
BuildRequires:	quazip-qt5-devel >= 0.6
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.605
# keep in sync with abi-version in -sip.patch (generated code must be compatible with sip.h taken from installed sip6 package)
BuildRequires:	sip6 >= 6.15.1
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xsimd-devel < 14
BuildRequires:	xsimd-devel >= 8.1.0
BuildRequires:	xz
BuildRequires:	zlib-devel
BuildRequires:	zug-devel
Requires:	%{name}-data = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Krita is a free and open source digital painting application. It is
for artists who want to create professional work from start to end.
Krita is used by comic book artists, illustrators, concept artists,
matte and texture painters and in the digital VFX industry.

%description -l pl.UTF-8
Krita to wolnodostępna, mająca otwarte źródła aplikacja do rysunków
cyfrowych. Jest przeznaczona dla artystów, chcących tworzyć
profesjonalne prace od początku do końca. Jest używana przez autorów
komiksów, ilustratorów, artystów koncepcyjnych, rysujących maty i
tekstury oraz w cyfrowym przemyśle VFX.

%package devel
Summary:	Header files for Krita libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek Krity
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for Krita libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek Krity.

%package data
Summary:	Data files for Krita application
Summary(pl.UTF-8):	Dane dla aplikacji Krita
Group:		X11/Applications/Graphics
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	shared-mime-info
BuildArch:	noarch

%description data
Data files for Krita application.

%description data -l pl.UTF-8
Dane dla aplikacji Krita.

%prep
%setup -q -n %{orgname}-%{version}
%patch -P 0 -p1

%build
%cmake -B build \
	-G Ninja \
	-DCMAKE_DISABLE_FIND_PACKAGE_KSeExpr=ON \
	-DCMAKE_DISABLE_FIND_PACKAGE_xsimd=ON \
	-DENABLE_UPDATERS=OFF \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_SYSCONFDIR=%{_sysconfdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DKRITA_ENABLE_PCH=OFF

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{orgname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post data
%update_mime_database
%update_desktop_database

%postun data
%update_mime_database
%update_desktop_database_postun

%files
%defattr(644,root,root,755)
/etc/xdg/kritarc
%attr(755,root,root) %{_bindir}/krita
%attr(755,root,root) %{_bindir}/krita_version
%attr(755,root,root) %{_bindir}/kritarunner
%attr(755,root,root) %{_libdir}/libkritabasicflakes.so.*.*.*
%ghost %{_libdir}/libkritabasicflakes.so.19
%attr(755,root,root) %{_libdir}/libkritacolor.so.*.*.*
%ghost %{_libdir}/libkritacolor.so.19
%attr(755,root,root) %{_libdir}/libkritacolord.so.*.*.*
%ghost %{_libdir}/libkritacolord.so.19
%attr(755,root,root) %{_libdir}/libkritacommand.so.*.*.*
%ghost %{_libdir}/libkritacommand.so.19
%attr(755,root,root) %{_libdir}/libkritaexifcommon.so.*.*.*
%ghost %{_libdir}/libkritaexifcommon.so.19
%attr(755,root,root) %{_libdir}/libkritaflake.so.*.*.*
%ghost %{_libdir}/libkritaflake.so.19
%attr(755,root,root) %{_libdir}/libkritaglobal.so.*.*.*
%ghost %{_libdir}/libkritaglobal.so.19
%attr(755,root,root) %{_libdir}/libkritaimage.so.*.*.*
%ghost %{_libdir}/libkritaimage.so.19
%attr(755,root,root) %{_libdir}/libkritaimpex.so.*.*.*
%ghost %{_libdir}/libkritaimpex.so.19
%attr(755,root,root) %{_libdir}/libkritalibbrush.so.*.*.*
%ghost %{_libdir}/libkritalibbrush.so.19
%attr(755,root,root) %{_libdir}/libkritalibkis.so.*.*.*
%ghost %{_libdir}/libkritalibkis.so.19
%attr(755,root,root) %{_libdir}/libkritalibkra.so.*.*.*
%ghost %{_libdir}/libkritalibkra.so.19
%attr(755,root,root) %{_libdir}/libkritalibpaintop.so.*.*.*
%ghost %{_libdir}/libkritalibpaintop.so.19
%attr(755,root,root) %{_libdir}/libkritametadata.so.*.*.*
%ghost %{_libdir}/libkritametadata.so.19
%attr(755,root,root) %{_libdir}/libkritamultiarch.so.*.*.*
%ghost %{_libdir}/libkritamultiarch.so.19
%attr(755,root,root) %{_libdir}/libkritapigment.so.*.*.*
%ghost %{_libdir}/libkritapigment.so.19
%attr(755,root,root) %{_libdir}/libkritaplugin.so.*.*.*
%ghost %{_libdir}/libkritaplugin.so.19
%attr(755,root,root) %{_libdir}/libkritapsd.so.*.*.*
%ghost %{_libdir}/libkritapsd.so.19
%attr(755,root,root) %{_libdir}/libkritapsdutils.so.*.*.*
%ghost %{_libdir}/libkritapsdutils.so.19
%attr(755,root,root) %{_libdir}/libkritaqmicinterface.so.*.*.*
%ghost %{_libdir}/libkritaqmicinterface.so.19
%attr(755,root,root) %{_libdir}/libkritaresources.so.*.*.*
%ghost %{_libdir}/libkritaresources.so.19
%attr(755,root,root) %{_libdir}/libkritaresourcewidgets.so.*.*.*
%ghost %{_libdir}/libkritaresourcewidgets.so.19
%attr(755,root,root) %{_libdir}/libkritastore.so.*.*.*
%ghost %{_libdir}/libkritastore.so.19
%attr(755,root,root) %{_libdir}/libkritatiffpsd.so.*.*.*
%ghost %{_libdir}/libkritatiffpsd.so.19
%attr(755,root,root) %{_libdir}/libkritaui.so.*.*.*
%ghost %{_libdir}/libkritaui.so.19
%attr(755,root,root) %{_libdir}/libkritaversion.so.*.*.*
%ghost %{_libdir}/libkritaversion.so.19
%attr(755,root,root) %{_libdir}/libkritawidgets.so.*.*.*
%ghost %{_libdir}/libkritawidgets.so.19
%attr(755,root,root) %{_libdir}/libkritawidgetutils.so.*.*.*
%ghost %{_libdir}/libkritawidgetutils.so.19
%dir %{_libdir}/krita-python-libs
%dir %{_libdir}/krita-python-libs/PyKrita
%{_libdir}/krita-python-libs/PyKrita/krita.pyi
%attr(755,root,root) %{_libdir}/krita-python-libs/PyKrita/krita.so
%{_libdir}/krita-python-libs/krita
%dir %{_libdir}/kritaplugins
%attr(755,root,root) %{_libdir}/kritaplugins/krita_colorspaces_extensions.so
%attr(755,root,root) %{_libdir}/kritaplugins/krita_flaketools.so
%attr(755,root,root) %{_libdir}/kritaplugins/krita_karbontools.so
%attr(755,root,root) %{_libdir}/kritaplugins/krita_raw_import.so
%attr(755,root,root) %{_libdir}/kritaplugins/krita_shape_image.so
%attr(755,root,root) %{_libdir}/kritaplugins/krita_shape_paths.so
%attr(755,root,root) %{_libdir}/kritaplugins/krita_tool_svgtext.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritaanimationdocker.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritaarrangedocker.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritaartisticcolorselector.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritaasccdl.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritaassistanttool.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritablurfilter.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritabrushexport.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritabrushimport.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritabuginfo.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritachanneldocker.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritaclonesarray.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritacolorgenerator.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritacolorrange.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritacolorselectorng.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritacolorsfilters.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritacolorsmudgepaintop.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritacolorspaceconversion.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritacompositiondocker.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritaconvertheighttonormalmap.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritaconvolutionfilters.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritacsvexport.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritacsvimport.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritacurvepaintop.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritadbexplorer.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritadefaultpaintops.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritadefaulttools.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritadeformpaintop.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritadigitalmixer.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritadodgeburn.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritaedgedetection.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritaembossfilter.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritaexample.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritaexif.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritaexperimentpaintop.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritaexrexport.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritaexrimport.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritaextensioncolorsfilters.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritafastcolortransferfilter.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritafilterop.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritagamutmask.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritagaussianhighpassfilter.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritagifexport.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritagifimport.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritagradientgenerator.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritagradientmap.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritagriddocker.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritagridpaintop.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritahairypaintop.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritahalftone.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritahatchingpaintop.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritaheifexport.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritaheifimport.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritaheightmapexport.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritaheightmapimport.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritahistogramdocker.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritahistorydocker.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritaimageenhancement.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritaimagesplit.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritaindexcolors.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritaiptc.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritajp2import.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritajpegexport.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritajpegimport.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritajxlexport.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritajxlimport.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritakraexport.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritakraimport.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritakrzexport.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritalayerdocker.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritalayergroupswitcher.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritalayersplit.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritalcmsengine.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritalevelfilter.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritalogdocker.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritalutdocker.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritametadataeditor.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritamodifyselection.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritamultigridpatterngenerator.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritamypaintop.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritanoisefilter.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritanormalize.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritaoffsetimage.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritaoilpaintfilter.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritaoraexport.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritaoraimport.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritaoverviewdocker.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritapalettedocker.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritapalettize.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritaparticlepaintop.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritapatterndocker.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritapatterngenerator.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritapdfimport.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritaphongbumpmap.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritapixelizefilter.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritapngexport.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritapngimport.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritaposterize.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritapresetdocker.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritapresethistory.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritapsdexport.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritapsdimport.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritapykrita.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritaqimageioexport.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritaqimageioimport.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritaqmic.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritaqmlexport.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritaraindropsfilter.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritarandompickfilter.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritarecorderdocker.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritaresettransparent.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritaresourcemanager.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritarotateimage.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritaroundcornersfilter.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritaroundmarkerpaintop.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritasamplescreencolor.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritascreentonegenerator.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritaselectiontools.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritaseparatechannels.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritashearimage.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritasimplexnoisegenerator.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritasketchpaintop.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritasmallcolorselector.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritasmalltilesfilter.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritasnapshotdocker.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritaspecificcolorselector.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritaspraypaintop.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritaspriterexport.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritastoryboarddocker.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritasvgcollectiondocker.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritasvgimport.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritatangentnormalpaintop.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritatasksetdocker.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritatgaexport.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritatgaimport.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritathreshold.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritatiffexport.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritatiffimport.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritatoolSmartPatch.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritatoolcrop.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritatooldyna.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritatoolencloseandfill.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritatoollazybrush.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritatoolpolygon.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritatoolpolyline.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritatooltransform.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritatouchdocker.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritaunsharpfilter.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritawavefilter.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritawaveletdecompose.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritawebpexport.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritawebpimport.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritawgcolorselector.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritaxcfimport.so
%attr(755,root,root) %{_libdir}/kritaplugins/kritaxmp.so

%files devel
%defattr(644,root,root,755)
%{_libdir}/libkritabasicflakes.so
%{_libdir}/libkritacolor.so
%{_libdir}/libkritacolord.so
%{_libdir}/libkritacommand.so
%{_libdir}/libkritaexifcommon.so
%{_libdir}/libkritaflake.so
%{_libdir}/libkritaglobal.so
%{_libdir}/libkritaimage.so
%{_libdir}/libkritaimpex.so
%{_libdir}/libkritalibbrush.so
%{_libdir}/libkritalibkis.so
%{_libdir}/libkritalibkra.so
%{_libdir}/libkritalibpaintop.so
%{_libdir}/libkritametadata.so
%{_libdir}/libkritamultiarch.so
%{_libdir}/libkritapigment.so
%{_libdir}/libkritaplugin.so
%{_libdir}/libkritapsd.so
%{_libdir}/libkritapsdutils.so
%{_libdir}/libkritaqmicinterface.so
%{_libdir}/libkritaresources.so
%{_libdir}/libkritaresourcewidgets.so
%{_libdir}/libkritastore.so
%{_libdir}/libkritatiffpsd.so
%{_libdir}/libkritaui.so
%{_libdir}/libkritaversion.so
%{_libdir}/libkritawidgets.so
%{_libdir}/libkritawidgetutils.so
%{_includedir}/kis_qmic_interface.h
%{_includedir}/kis_qmic_plugin_interface.h
%{_includedir}/kritaqmicinterface_export.h

%files data -f %{orgname}.lang
%defattr(644,root,root,755)
%{_desktopdir}/krita_brush.desktop
%{_desktopdir}/krita_csv.desktop
%{_desktopdir}/krita_exr.desktop
%{_desktopdir}/krita_gif.desktop
%{_desktopdir}/krita_heif.desktop
%{_desktopdir}/krita_heightmap.desktop
%{_desktopdir}/krita_jp2.desktop
%{_desktopdir}/krita_jpeg.desktop
%{_desktopdir}/krita_jxl.desktop
%{_desktopdir}/krita_kra.desktop
%{_desktopdir}/krita_krz.desktop
%{_desktopdir}/krita_ora.desktop
%{_desktopdir}/krita_pdf.desktop
%{_desktopdir}/krita_png.desktop
%{_desktopdir}/krita_psd.desktop
%{_desktopdir}/krita_qimageio.desktop
%{_desktopdir}/krita_raw.desktop
%{_desktopdir}/krita_spriter.desktop
%{_desktopdir}/krita_svg.desktop
%{_desktopdir}/krita_tga.desktop
%{_desktopdir}/krita_tiff.desktop
%{_desktopdir}/krita_webp.desktop
%{_desktopdir}/krita_xcf.desktop
%{_desktopdir}/org.kde.krita.desktop
%{_datadir}/color-schemes/KritaBlender.colors
%{_datadir}/color-schemes/KritaBright.colors
%{_datadir}/color-schemes/KritaDark.colors
%{_datadir}/color-schemes/KritaDarkOrange.colors
%{_datadir}/color-schemes/KritaDarker.colors
%{_datadir}/color-schemes/KritaNeutral.colors
%{_datadir}/color/icc/krita
%{_iconsdir}/hicolor/1024x1024/apps/krita.png
%{_iconsdir}/hicolor/1024x1024/mimetypes/application-x-krita.png
%{_iconsdir}/hicolor/128x128/apps/krita.png
%{_iconsdir}/hicolor/128x128/mimetypes/application-x-krita.png
%{_iconsdir}/hicolor/16x16/apps/krita.png
%{_iconsdir}/hicolor/16x16/mimetypes/application-x-krita.png
%{_iconsdir}/hicolor/22x22/apps/krita.png
%{_iconsdir}/hicolor/22x22/mimetypes/application-x-krita.png
%{_iconsdir}/hicolor/256x256/apps/krita.png
%{_iconsdir}/hicolor/256x256/mimetypes/application-x-krita.png
%{_iconsdir}/hicolor/32x32/apps/krita.png
%{_iconsdir}/hicolor/32x32/mimetypes/application-x-krita.png
%{_iconsdir}/hicolor/48x48/apps/krita.png
%{_iconsdir}/hicolor/48x48/mimetypes/application-x-krita.png
%{_iconsdir}/hicolor/512x512/apps/krita.png
%{_iconsdir}/hicolor/512x512/mimetypes/application-x-krita.png
%{_iconsdir}/hicolor/64x64/apps/krita.png
%{_iconsdir}/hicolor/64x64/mimetypes/application-x-krita.png
%{_iconsdir}/hicolor/scalable/apps/krita.svgz
%{_datadir}/krita
%{_datadir}/kritaplugins
%{_datadir}/metainfo/org.kde.krita.appdata.xml
