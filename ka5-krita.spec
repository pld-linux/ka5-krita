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
Version:	5.2.16
Release:	2
License:	GPL v3+
Group:		X11/Applications/Graphics
Source0:	https://download.kde.org/%{_state}/krita/%{version}/%{orgname}-%{version}.tar.xz
# Source0-md5:	33356feacb69e575e66e2f2c620d3299
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
%{_libdir}/libkritabasicflakes.so.*.*.*
%ghost %{_libdir}/libkritabasicflakes.so.19
%{_libdir}/libkritacolor.so.*.*.*
%ghost %{_libdir}/libkritacolor.so.19
%{_libdir}/libkritacolord.so.*.*.*
%ghost %{_libdir}/libkritacolord.so.19
%{_libdir}/libkritacommand.so.*.*.*
%ghost %{_libdir}/libkritacommand.so.19
%{_libdir}/libkritaexifcommon.so.*.*.*
%ghost %{_libdir}/libkritaexifcommon.so.19
%{_libdir}/libkritaflake.so.*.*.*
%ghost %{_libdir}/libkritaflake.so.19
%{_libdir}/libkritaglobal.so.*.*.*
%ghost %{_libdir}/libkritaglobal.so.19
%{_libdir}/libkritaimage.so.*.*.*
%ghost %{_libdir}/libkritaimage.so.19
%{_libdir}/libkritaimpex.so.*.*.*
%ghost %{_libdir}/libkritaimpex.so.19
%{_libdir}/libkritalibbrush.so.*.*.*
%ghost %{_libdir}/libkritalibbrush.so.19
%{_libdir}/libkritalibkis.so.*.*.*
%ghost %{_libdir}/libkritalibkis.so.19
%{_libdir}/libkritalibkra.so.*.*.*
%ghost %{_libdir}/libkritalibkra.so.19
%{_libdir}/libkritalibpaintop.so.*.*.*
%ghost %{_libdir}/libkritalibpaintop.so.19
%{_libdir}/libkritametadata.so.*.*.*
%ghost %{_libdir}/libkritametadata.so.19
%{_libdir}/libkritamultiarch.so.*.*.*
%ghost %{_libdir}/libkritamultiarch.so.19
%{_libdir}/libkritapigment.so.*.*.*
%ghost %{_libdir}/libkritapigment.so.19
%{_libdir}/libkritaplugin.so.*.*.*
%ghost %{_libdir}/libkritaplugin.so.19
%{_libdir}/libkritapsd.so.*.*.*
%ghost %{_libdir}/libkritapsd.so.19
%{_libdir}/libkritapsdutils.so.*.*.*
%ghost %{_libdir}/libkritapsdutils.so.19
%{_libdir}/libkritaqmicinterface.so.*.*.*
%ghost %{_libdir}/libkritaqmicinterface.so.19
%{_libdir}/libkritaresources.so.*.*.*
%ghost %{_libdir}/libkritaresources.so.19
%{_libdir}/libkritaresourcewidgets.so.*.*.*
%ghost %{_libdir}/libkritaresourcewidgets.so.19
%{_libdir}/libkritastore.so.*.*.*
%ghost %{_libdir}/libkritastore.so.19
%{_libdir}/libkritatiffpsd.so.*.*.*
%ghost %{_libdir}/libkritatiffpsd.so.19
%{_libdir}/libkritaui.so.*.*.*
%ghost %{_libdir}/libkritaui.so.19
%{_libdir}/libkritaversion.so.*.*.*
%ghost %{_libdir}/libkritaversion.so.19
%{_libdir}/libkritawidgets.so.*.*.*
%ghost %{_libdir}/libkritawidgets.so.19
%{_libdir}/libkritawidgetutils.so.*.*.*
%ghost %{_libdir}/libkritawidgetutils.so.19
%dir %{_libdir}/krita-python-libs
%dir %{_libdir}/krita-python-libs/PyKrita
%{_libdir}/krita-python-libs/PyKrita/krita.pyi
%{_libdir}/krita-python-libs/PyKrita/krita.so
%{_libdir}/krita-python-libs/krita
%dir %{_libdir}/kritaplugins
%{_libdir}/kritaplugins/krita_colorspaces_extensions.so
%{_libdir}/kritaplugins/krita_flaketools.so
%{_libdir}/kritaplugins/krita_karbontools.so
%{_libdir}/kritaplugins/krita_raw_import.so
%{_libdir}/kritaplugins/krita_shape_image.so
%{_libdir}/kritaplugins/krita_shape_paths.so
%{_libdir}/kritaplugins/krita_tool_svgtext.so
%{_libdir}/kritaplugins/kritaanimationdocker.so
%{_libdir}/kritaplugins/kritaarrangedocker.so
%{_libdir}/kritaplugins/kritaartisticcolorselector.so
%{_libdir}/kritaplugins/kritaasccdl.so
%{_libdir}/kritaplugins/kritaassistanttool.so
%{_libdir}/kritaplugins/kritablurfilter.so
%{_libdir}/kritaplugins/kritabrushexport.so
%{_libdir}/kritaplugins/kritabrushimport.so
%{_libdir}/kritaplugins/kritabuginfo.so
%{_libdir}/kritaplugins/kritachanneldocker.so
%{_libdir}/kritaplugins/kritaclonesarray.so
%{_libdir}/kritaplugins/kritacolorgenerator.so
%{_libdir}/kritaplugins/kritacolorrange.so
%{_libdir}/kritaplugins/kritacolorselectorng.so
%{_libdir}/kritaplugins/kritacolorsfilters.so
%{_libdir}/kritaplugins/kritacolorsmudgepaintop.so
%{_libdir}/kritaplugins/kritacolorspaceconversion.so
%{_libdir}/kritaplugins/kritacompositiondocker.so
%{_libdir}/kritaplugins/kritaconvertheighttonormalmap.so
%{_libdir}/kritaplugins/kritaconvolutionfilters.so
%{_libdir}/kritaplugins/kritacsvexport.so
%{_libdir}/kritaplugins/kritacsvimport.so
%{_libdir}/kritaplugins/kritacurvepaintop.so
%{_libdir}/kritaplugins/kritadbexplorer.so
%{_libdir}/kritaplugins/kritadefaultpaintops.so
%{_libdir}/kritaplugins/kritadefaulttools.so
%{_libdir}/kritaplugins/kritadeformpaintop.so
%{_libdir}/kritaplugins/kritadigitalmixer.so
%{_libdir}/kritaplugins/kritadodgeburn.so
%{_libdir}/kritaplugins/kritaedgedetection.so
%{_libdir}/kritaplugins/kritaembossfilter.so
%{_libdir}/kritaplugins/kritaexample.so
%{_libdir}/kritaplugins/kritaexif.so
%{_libdir}/kritaplugins/kritaexperimentpaintop.so
%{_libdir}/kritaplugins/kritaexrexport.so
%{_libdir}/kritaplugins/kritaexrimport.so
%{_libdir}/kritaplugins/kritaextensioncolorsfilters.so
%{_libdir}/kritaplugins/kritafastcolortransferfilter.so
%{_libdir}/kritaplugins/kritafilterop.so
%{_libdir}/kritaplugins/kritagamutmask.so
%{_libdir}/kritaplugins/kritagaussianhighpassfilter.so
%{_libdir}/kritaplugins/kritagifexport.so
%{_libdir}/kritaplugins/kritagifimport.so
%{_libdir}/kritaplugins/kritagradientgenerator.so
%{_libdir}/kritaplugins/kritagradientmap.so
%{_libdir}/kritaplugins/kritagriddocker.so
%{_libdir}/kritaplugins/kritagridpaintop.so
%{_libdir}/kritaplugins/kritahairypaintop.so
%{_libdir}/kritaplugins/kritahalftone.so
%{_libdir}/kritaplugins/kritahatchingpaintop.so
%{_libdir}/kritaplugins/kritaheifexport.so
%{_libdir}/kritaplugins/kritaheifimport.so
%{_libdir}/kritaplugins/kritaheightmapexport.so
%{_libdir}/kritaplugins/kritaheightmapimport.so
%{_libdir}/kritaplugins/kritahistogramdocker.so
%{_libdir}/kritaplugins/kritahistorydocker.so
%{_libdir}/kritaplugins/kritaimageenhancement.so
%{_libdir}/kritaplugins/kritaimagesplit.so
%{_libdir}/kritaplugins/kritaindexcolors.so
%{_libdir}/kritaplugins/kritaiptc.so
%{_libdir}/kritaplugins/kritajp2import.so
%{_libdir}/kritaplugins/kritajpegexport.so
%{_libdir}/kritaplugins/kritajpegimport.so
%{_libdir}/kritaplugins/kritajxlexport.so
%{_libdir}/kritaplugins/kritajxlimport.so
%{_libdir}/kritaplugins/kritakraexport.so
%{_libdir}/kritaplugins/kritakraimport.so
%{_libdir}/kritaplugins/kritakrzexport.so
%{_libdir}/kritaplugins/kritalayerdocker.so
%{_libdir}/kritaplugins/kritalayergroupswitcher.so
%{_libdir}/kritaplugins/kritalayersplit.so
%{_libdir}/kritaplugins/kritalcmsengine.so
%{_libdir}/kritaplugins/kritalevelfilter.so
%{_libdir}/kritaplugins/kritalogdocker.so
%{_libdir}/kritaplugins/kritalutdocker.so
%{_libdir}/kritaplugins/kritametadataeditor.so
%{_libdir}/kritaplugins/kritamodifyselection.so
%{_libdir}/kritaplugins/kritamultigridpatterngenerator.so
%{_libdir}/kritaplugins/kritamypaintop.so
%{_libdir}/kritaplugins/kritanoisefilter.so
%{_libdir}/kritaplugins/kritanormalize.so
%{_libdir}/kritaplugins/kritaoffsetimage.so
%{_libdir}/kritaplugins/kritaoilpaintfilter.so
%{_libdir}/kritaplugins/kritaoraexport.so
%{_libdir}/kritaplugins/kritaoraimport.so
%{_libdir}/kritaplugins/kritaoverviewdocker.so
%{_libdir}/kritaplugins/kritapalettedocker.so
%{_libdir}/kritaplugins/kritapalettize.so
%{_libdir}/kritaplugins/kritaparticlepaintop.so
%{_libdir}/kritaplugins/kritapatterndocker.so
%{_libdir}/kritaplugins/kritapatterngenerator.so
%{_libdir}/kritaplugins/kritapdfimport.so
%{_libdir}/kritaplugins/kritaphongbumpmap.so
%{_libdir}/kritaplugins/kritapixelizefilter.so
%{_libdir}/kritaplugins/kritapngexport.so
%{_libdir}/kritaplugins/kritapngimport.so
%{_libdir}/kritaplugins/kritaposterize.so
%{_libdir}/kritaplugins/kritapresetdocker.so
%{_libdir}/kritaplugins/kritapresethistory.so
%{_libdir}/kritaplugins/kritapsdexport.so
%{_libdir}/kritaplugins/kritapsdimport.so
%{_libdir}/kritaplugins/kritapykrita.so
%{_libdir}/kritaplugins/kritaqimageioexport.so
%{_libdir}/kritaplugins/kritaqimageioimport.so
%{_libdir}/kritaplugins/kritaqmic.so
%{_libdir}/kritaplugins/kritaqmlexport.so
%{_libdir}/kritaplugins/kritaraindropsfilter.so
%{_libdir}/kritaplugins/kritarandompickfilter.so
%{_libdir}/kritaplugins/kritarecorderdocker.so
%{_libdir}/kritaplugins/kritaresettransparent.so
%{_libdir}/kritaplugins/kritaresourcemanager.so
%{_libdir}/kritaplugins/kritarotateimage.so
%{_libdir}/kritaplugins/kritaroundcornersfilter.so
%{_libdir}/kritaplugins/kritaroundmarkerpaintop.so
%{_libdir}/kritaplugins/kritasamplescreencolor.so
%{_libdir}/kritaplugins/kritascreentonegenerator.so
%{_libdir}/kritaplugins/kritaselectiontools.so
%{_libdir}/kritaplugins/kritaseparatechannels.so
%{_libdir}/kritaplugins/kritashearimage.so
%{_libdir}/kritaplugins/kritasimplexnoisegenerator.so
%{_libdir}/kritaplugins/kritasketchpaintop.so
%{_libdir}/kritaplugins/kritasmallcolorselector.so
%{_libdir}/kritaplugins/kritasmalltilesfilter.so
%{_libdir}/kritaplugins/kritasnapshotdocker.so
%{_libdir}/kritaplugins/kritaspecificcolorselector.so
%{_libdir}/kritaplugins/kritaspraypaintop.so
%{_libdir}/kritaplugins/kritaspriterexport.so
%{_libdir}/kritaplugins/kritastoryboarddocker.so
%{_libdir}/kritaplugins/kritasvgcollectiondocker.so
%{_libdir}/kritaplugins/kritasvgimport.so
%{_libdir}/kritaplugins/kritatangentnormalpaintop.so
%{_libdir}/kritaplugins/kritatasksetdocker.so
%{_libdir}/kritaplugins/kritatgaexport.so
%{_libdir}/kritaplugins/kritatgaimport.so
%{_libdir}/kritaplugins/kritathreshold.so
%{_libdir}/kritaplugins/kritatiffexport.so
%{_libdir}/kritaplugins/kritatiffimport.so
%{_libdir}/kritaplugins/kritatoolSmartPatch.so
%{_libdir}/kritaplugins/kritatoolcrop.so
%{_libdir}/kritaplugins/kritatooldyna.so
%{_libdir}/kritaplugins/kritatoolencloseandfill.so
%{_libdir}/kritaplugins/kritatoollazybrush.so
%{_libdir}/kritaplugins/kritatoolpolygon.so
%{_libdir}/kritaplugins/kritatoolpolyline.so
%{_libdir}/kritaplugins/kritatooltransform.so
%{_libdir}/kritaplugins/kritatouchdocker.so
%{_libdir}/kritaplugins/kritaunsharpfilter.so
%{_libdir}/kritaplugins/kritawavefilter.so
%{_libdir}/kritaplugins/kritawaveletdecompose.so
%{_libdir}/kritaplugins/kritawebpexport.so
%{_libdir}/kritaplugins/kritawebpimport.so
%{_libdir}/kritaplugins/kritawgcolorselector.so
%{_libdir}/kritaplugins/kritaxcfimport.so
%{_libdir}/kritaplugins/kritaxmp.so

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
