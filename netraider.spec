Summary:	embedded version of KDE's konqueror browser
Summary(pl):	minimalna wersja przegl±darki konquerror pochodz±cej z KDE
Name:		netraider
Version:	0.0.2
Release:	5
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://mandragon.org/raider/%{name}-source-%{version}.tar.gz
# Source0-md5:	301b43a32acf49bd8295cbc54b4dd1e7
URL:		http://mandragon.org/raider/
BuildRequires:	libpng-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libstdc++-devel
BuildRequires:	openssl-devel >= 0.9.7
BuildRequires:	zlib-devel
BuildRequires:	qt-devel >= 2.2.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Small desktop independent web browser witch features such as: cookie
management, bookmarks, javascript support, proxy support, SSL support.

%description -l pl
Niewielka, niezale¿na od zarz±dcy okien przegl±darka www z takimi
mo¿liwo¶ciami jak: zarz±dzanie ciasteczkami, ksi±¿ki adresowe,
wsparcie dla javascript, proxy oraz SSL.

%prep
%setup -q -n %{name}-source-%{version}

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_prefix}/konq	$RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
