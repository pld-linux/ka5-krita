#
# Conditional build:
#
%define		_state		stable
%define		qtver		5.5.1
%define		orgname		krita

Summary:	A digital painting application
Name:		ka5-krita
Version:	5.1.2
Release:	1
License:	GPL v3+
Group:		X11/Applications/Graphics
Source0:	https://download.kde.org/%{_state}/krita/%{version}/%{orgname}-%{version}.tar.xz
# Source0-md5:	f89ab0c81d99bd7f48ebac66e99c767f
URL:		https://www.krita.org/
BuildRequires:	OpenColorIO-devel
BuildRequires:	OpenEXR-devel
BuildRequires:	Qt5Concurrent-devel
BuildRequires:	Qt5Core-devel >= 5.15.2
BuildRequires:	Qt5DBus-devel >= 5.9.0
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Multimedia-devel
BuildRequires:	Qt5Multimedia-devel >= 5.9.0
BuildRequires:	Qt5Network-devel
BuildRequires:	Qt5PrintSupport-devel
BuildRequires:	Qt5Qml-devel >= 5.15.2
BuildRequires:	Qt5Quick-devel >= 5.9.0
BuildRequires:	Qt5Sql-devel
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	Qt5X11Extras-devel
BuildRequires:	Qt5Xml-devel
BuildRequires:	boost-devel >= 1.55
BuildRequires:	cmake >= 2.8.9
BuildRequires:	eigen3 >= 3.0
BuildRequires:	exiv2-devel >= 0.16
BuildRequires:	fftw3-devel
BuildRequires:	gettext-devel
BuildRequires:	giflib-devel
BuildRequires:	gsl-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.22
BuildRequires:	kf5-kcompletion-devel >= 5.44.0
BuildRequires:	kf5-kconfig-devel >= 5.44.0
BuildRequires:	kf5-kcoreaddons-devel >= 5.44.0
BuildRequires:	kf5-kcrash-devel >= 5.44.0
BuildRequires:	kf5-kguiaddons-devel >= 5.44.0
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-kitemmodels-devel >= 5.44.0
BuildRequires:	kf5-kitemviews-devel >= 5.44.0
BuildRequires:	kf5-kwidgetsaddons-devel >= 5.44.0
BuildRequires:	kf5-kwindowsystem-devel >= 5.44.0
BuildRequires:	lcms2-devel >= 2.4
BuildRequires:	libheif-devel >= 1.10.0
BuildRequires:	libjpeg-turbo-devel
BuildRequires:	libmypaint-devel
BuildRequires:	libpng-devel
BuildRequires:	libraw-devel >= 0.16
BuildRequires:	libtiff-devel
BuildRequires:	libwebp-devel >= 1.2.0
BuildRequires:	ninja
BuildRequires:	openjpeg2-devel >= 2.3.0
BuildRequires:	pkgconfig
BuildRequires:	poppler-qt5-devel
BuildRequires:	python3-PyQt5 >= 5.6.0
BuildRequires:	python3-devel
BuildRequires:	quazip-qt5-devel
BuildRequires:	sip-PyQt5
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires:	%{name}-data = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Krita is a free and open source digital painting application. It is
for artists who want to create professional work from start to end.
Krita is used by comic book artists, illustrators, concept artists,
matte and texture painters and in the digital VFX industry.

%package data
Summary:	Data files for %{kaname}
Summary(pl.UTF-8):	Dane dla %{kaname}
Group:		X11/Applications/Games
BuildArch:	noarch
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	shared-mime-info

%description data
Data files for %{kaname}.

%description data -l pl.UTF-8
Dane dla %{kaname}.


%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%{__sed} -i -e 's|!/usr/bin/env python3|!/usr/bin/python3|' $RPM_BUILD_ROOT%{_bindir}/AppImageUpdateDummy

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/x-test

%find_lang %{orgname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%post data
%update_mime_database
%update_desktop_database

%postun data
%update_mime_database
%update_desktop_database_postun

%files
%defattr(644,root,root,755)
/etc/xdg/kritarc
%attr(755,root,root) %{_bindir}/AppImageUpdateDummy
%attr(755,root,root) %{_bindir}/krita
%attr(755,root,root) %{_bindir}/krita_version
%attr(755,root,root) %{_bindir}/kritarunner
%{_includedir}/kis_qmic_interface.h
%{_includedir}/kis_qmic_plugin_interface.h
%{_includedir}/kritaqmicinterface_export.h
%dir %{_libdir}/krita-python-libs
%dir %{_libdir}/krita-python-libs/PyKrita
%{_libdir}/krita-python-libs/PyKrita/krita.so
%{_libdir}/krita-python-libs/krita/__init__.py
%dir %{_libdir}/krita-python-libs/krita
%{_libdir}/krita-python-libs/krita/api.py
%dir %{_libdir}/krita-python-libs/krita/attic
%{_libdir}/krita-python-libs/krita/attic/mikro.py
%{_libdir}/krita-python-libs/krita/attic/scripter_hooks.py
%{_libdir}/krita-python-libs/krita/decorators.py
%{_libdir}/krita-python-libs/krita/dockwidgetfactory.py
%{_libdir}/krita-python-libs/krita/excepthook.py
%{_libdir}/krita-python-libs/krita/excepthook_ui.py
%dir %{_libdir}/krita-python-libs/krita/sceditor
%{_libdir}/krita-python-libs/krita/sceditor/__init__.py
%{_libdir}/krita-python-libs/krita/sceditor/assist.py
%{_libdir}/krita-python-libs/krita/sceditor/console.py
%{_libdir}/krita-python-libs/krita/sceditor/dockwidget.py
%{_libdir}/krita-python-libs/krita/sceditor/dockwidget_icons.py
%{_libdir}/krita-python-libs/krita/sceditor/highlighter.py
%{_libdir}/krita-python-libs/krita/sceditor/indenter.py
%{_libdir}/krita-python-libs/krita/sceditor/mainwindow.py
%{_libdir}/krita-python-libs/krita/sceditor/mainwindow_ui.py
%{_libdir}/krita-python-libs/krita/sceditor/widget.py
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
%{_libdir}/kritaplugins/kritaresourcemanager.so
%{_libdir}/kritaplugins/kritarotateimage.so
%{_libdir}/kritaplugins/kritaroundcornersfilter.so
%{_libdir}/kritaplugins/kritaroundmarkerpaintop.so
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
%{_libdir}/kritaplugins/kritaxcfimport.so
%{_libdir}/kritaplugins/kritaxmp.so
%{_libdir}/libkritabasicflakes.so
%ghost %{_libdir}/libkritabasicflakes.so.18
%{_libdir}/libkritabasicflakes.so.*.*.*
%{_libdir}/libkritacolor.so
%ghost %{_libdir}/libkritacolor.so.18
%{_libdir}/libkritacolor.so.*.*.*
%{_libdir}/libkritacolord.so
%ghost %{_libdir}/libkritacolord.so.18
%{_libdir}/libkritacolord.so.*.*.*
%{_libdir}/libkritacommand.so
%ghost %{_libdir}/libkritacommand.so.18
%{_libdir}/libkritacommand.so.*.*.*
%{_libdir}/libkritaflake.so
%ghost %{_libdir}/libkritaflake.so.18
%{_libdir}/libkritaflake.so.*.*.*
%{_libdir}/libkritaglobal.so
%ghost %{_libdir}/libkritaglobal.so.18
%{_libdir}/libkritaglobal.so.*.*.*
%{_libdir}/libkritaimage.so
%ghost %{_libdir}/libkritaimage.so.18
%{_libdir}/libkritaimage.so.*.*.*
%{_libdir}/libkritaimpex.so
%ghost %{_libdir}/libkritaimpex.so.18
%{_libdir}/libkritaimpex.so.*.*.*
%{_libdir}/libkritalibbrush.so
%ghost %{_libdir}/libkritalibbrush.so.18
%{_libdir}/libkritalibbrush.so.*.*.*
%{_libdir}/libkritalibkis.so
%ghost %{_libdir}/libkritalibkis.so.18
%{_libdir}/libkritalibkis.so.*.*.*
%{_libdir}/libkritalibkra.so
%ghost %{_libdir}/libkritalibkra.so.18
%{_libdir}/libkritalibkra.so.*.*.*
%{_libdir}/libkritalibpaintop.so
%ghost %{_libdir}/libkritalibpaintop.so.18
%{_libdir}/libkritalibpaintop.so.*.*.*
%{_libdir}/libkritametadata.so
%ghost %{_libdir}/libkritametadata.so.18
%{_libdir}/libkritametadata.so.*.*.*
%{_libdir}/libkritapigment.so
%ghost %{_libdir}/libkritapigment.so.18
%{_libdir}/libkritapigment.so.*.*.*
%{_libdir}/libkritaplugin.so
%ghost %{_libdir}/libkritaplugin.so.18
%{_libdir}/libkritaplugin.so.*.*.*
%{_libdir}/libkritapsd.so
%ghost %{_libdir}/libkritapsd.so.18
%{_libdir}/libkritapsd.so.*.*.*
%{_libdir}/libkritapsdutils.so
%ghost %{_libdir}/libkritapsdutils.so.18
%{_libdir}/libkritapsdutils.so.*.*.*
%{_libdir}/libkritaqmicinterface.so
%ghost %{_libdir}/libkritaqmicinterface.so.18
%{_libdir}/libkritaqmicinterface.so.*.*.*
%{_libdir}/libkritaqml.so
%ghost %{_libdir}/libkritaqml.so.18
%{_libdir}/libkritaqml.so.*.*.*
%{_libdir}/libkritaresources.so
%ghost %{_libdir}/libkritaresources.so.18
%{_libdir}/libkritaresources.so.*.*.*
%{_libdir}/libkritaresourcewidgets.so
%ghost %{_libdir}/libkritaresourcewidgets.so.18
%{_libdir}/libkritaresourcewidgets.so.*.*.*
%{_libdir}/libkritastore.so
%ghost %{_libdir}/libkritastore.so.18
%{_libdir}/libkritastore.so.*.*.*
%{_libdir}/libkritatiffpsd.so
%ghost %{_libdir}/libkritatiffpsd.so.18
%{_libdir}/libkritatiffpsd.so.*.*.*
%{_libdir}/libkritaui.so
%ghost %{_libdir}/libkritaui.so.18
%{_libdir}/libkritaui.so.*.*.*
%{_libdir}/libkritaversion.so
%ghost %{_libdir}/libkritaversion.so.18
%{_libdir}/libkritaversion.so.*.*.*
%{_libdir}/libkritawidgets.so
%ghost %{_libdir}/libkritawidgets.so.18
%{_libdir}/libkritawidgets.so.*.*.*
%{_libdir}/libkritawidgetutils.so
%ghost %{_libdir}/libkritawidgetutils.so.18
%{_libdir}/libkritawidgetutils.so.*.*.*
%dir %{_libdir}/qt5/qml/org/krita
%dir %{_libdir}/qt5/qml/org/krita/draganddrop
%{_libdir}/qt5/qml/org/krita/draganddrop/libdraganddropplugin.so
%{_libdir}/qt5/qml/org/krita/draganddrop/qmldir
%dir %{_libdir}/qt5/qml/org/krita/sketch
%dir %{_libdir}/qt5/qml/org/krita/sketch/components
%{_libdir}/qt5/qml/org/krita/sketch/components/BusyIndicator.qml
%{_libdir}/qt5/qml/org/krita/sketch/components/Button.qml
%{_libdir}/qt5/qml/org/krita/sketch/components/ButtonSquared.qml
%{_libdir}/qt5/qml/org/krita/sketch/components/CategorySwitcher.qml
%{_libdir}/qt5/qml/org/krita/sketch/components/CheckBox.qml
%{_libdir}/qt5/qml/org/krita/sketch/components/ColorSwatch.qml
%{_libdir}/qt5/qml/org/krita/sketch/components/Dialog.qml
%{_libdir}/qt5/qml/org/krita/sketch/components/Divider.qml
%{_libdir}/qt5/qml/org/krita/sketch/components/DropShadow.qml
%{_libdir}/qt5/qml/org/krita/sketch/components/ExpandingListView.qml
%{_libdir}/qt5/qml/org/krita/sketch/components/Header.qml
%{_libdir}/qt5/qml/org/krita/sketch/components/Label.qml
%{_libdir}/qt5/qml/org/krita/sketch/components/ListItem.qml
%{_libdir}/qt5/qml/org/krita/sketch/components/MessageStack.qml
%{_libdir}/qt5/qml/org/krita/sketch/components/NewImageList.qml
%{_libdir}/qt5/qml/org/krita/sketch/components/NewsList.qml
%{_libdir}/qt5/qml/org/krita/sketch/components/Page.qml
%{_libdir}/qt5/qml/org/krita/sketch/components/PageStack.js
%{_libdir}/qt5/qml/org/krita/sketch/components/PageStack.qml
%{_libdir}/qt5/qml/org/krita/sketch/components/PanelTextField.qml
%{_libdir}/qt5/qml/org/krita/sketch/components/RangeCombo.qml
%{_libdir}/qt5/qml/org/krita/sketch/components/RangeInput.qml
%{_libdir}/qt5/qml/org/krita/sketch/components/RecentFilesList.qml
%{_libdir}/qt5/qml/org/krita/sketch/components/ScrollDecorator.qml
%{_libdir}/qt5/qml/org/krita/sketch/components/Shadow.qml
%{_libdir}/qt5/qml/org/krita/sketch/components/Slider.qml
%{_libdir}/qt5/qml/org/krita/sketch/components/TextField.qml
%{_libdir}/qt5/qml/org/krita/sketch/components/TextFieldMultiline.qml
%{_libdir}/qt5/qml/org/krita/sketch/components/Tooltip.qml
%{_libdir}/qt5/qml/org/krita/sketch/components/VirtualKeyboard.qml
%{_libdir}/qt5/qml/org/krita/sketch/components/qmldir
%{_libdir}/qt5/qml/org/krita/sketch/libkritasketchplugin.so
%{_libdir}/qt5/qml/org/krita/sketch/qmldir

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
