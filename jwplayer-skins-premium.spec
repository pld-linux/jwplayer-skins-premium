Summary:	Premium skins for jwplayer
Name:		jwplayer-skins-premium
# no versioning, just use current jwplayer version they worked with
Version:	6.9
Release:	1
# zip is called "premium", but no licensing information can be found
License:	?
Group:		Applications/WWW
Source0:	https://account.jwplayer.com/static/download/%{name}.zip
# NoSource0-md5:	fbf963f636cebbfe06a9fbb2de19870e
NoSource:	0
URL:		http://www.jwplayer.com/skins/
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	unzip
Requires:	jwplayer >= 6.9
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_webapp	jwplayer
%define		_appdir	%{_datadir}/%{_webapp}

%description
Premium skins for JW Media Player.

%prep
%setup -qc
mv %{name} skins

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -a skins $RPM_BUILD_ROOT%{_appdir}

# these are "free" skins, available in base package
%{__rm} $RPM_BUILD_ROOT%{_appdir}/skins/five.xml
%{__rm} $RPM_BUILD_ROOT%{_appdir}/skins/six.xml

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_appdir}/skins/beelden.xml
%{_appdir}/skins/bekle.xml
%{_appdir}/skins/glow.xml
%{_appdir}/skins/modieus.xml
%{_appdir}/skins/roundster.xml
%{_appdir}/skins/stormtrooper.xml
%{_appdir}/skins/vapor.xml
