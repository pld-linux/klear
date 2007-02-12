Summary:	Klear - DVB TV viewer
Summary(pl.UTF-8):	Klear - odtwarzacz DVB TV
Name:		klear
Version:	0.6.0
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://www.tr0ll.net/kraus.tk/projects/klear/sources/%{name}-%{version}.tar.gz
# Source0-md5:	90889c1cbef48a7ffaf41e3bce39781c
URL:		http://www.klear.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	scons
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Klear is a DVB TV viewer and harddiskrecorder for Linux. It includes
internal tuners for DVB-S, DVB-S and DVB-T, a recodering system (live
and scheduled recording) with different recording formats,
screenshots, deinterlacing and different backend engines. Klear also
includes a complete SI-based EPG.

%description -l pl.UTF-8
Klear to odtwarzacz DVB TV oraz nagrywarka dyskowa dla Linuksa.
Zawiera wewnętrzne tunery dla DVB-S, DVB-S i DVB-T, system nagrywania
(na żywo i z opóźnieniem) z różnymi formatami nagrywania, zrzuty
ekranu, tryb bezprzeplotowy i różne wtyczki wyjściowe. Klear zawiera
również kompletny EPG oparty na SI.

%prep
%setup -q

%build
scons \
	qtincludes=%{_includedir}/qt

%install
rm -rf $RPM_BUILD_ROOT

scons install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir} \
	kdelnkdir=%{_desktopdir} \

install -d $RPM_BUILD_ROOT%{_desktopdir}/kde
mv -f $RPM_BUILD_ROOT%{_datadir}/applnk/Multimedia/klear.desktop \
	$RPM_BUILD_ROOT%{_desktopdir}/kde

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/klear
%{_datadir}/apps/klear
%{_desktopdir}/kde/klear.desktop
%{_iconsdir}/hicolor/*/apps/klear.png
