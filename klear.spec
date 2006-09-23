%define		_ver	alpha1
Summary:	Klear
Summary(pl):	Klear
Name:		klear
Version:	0.6.0
Release:	0.%{_ver}.1
License:	GPL
Group:		X11/Applications
Source0:	http://www.tr0ll.net/kraus.tk/projects/klear/sources/%{name}-%{version}-%{_ver}.tar.gz
# Source0-md5:	2b699a1884bbe08958299a65a4a59615
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
screenshots, deinterlacing and different backend engines.Klear also
includes a complete SI-based EPG.

#%description -l pl

%prep
%setup -q -n %{name}-%{version}-%{_ver}

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

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/klear
%{_datadir}/applnk/Multimedia/klear.desktop
%dir %{_datadir}/apps/klear
%{_datadir}/apps/klear
%{_iconsdir}/hicolor/*/apps/klear.png
