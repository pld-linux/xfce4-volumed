Summary:	Volume management daemon for XFCE
Summary(pl.UTF-8):	Demon poziomu dźwięku XFCE
Name:		xfce4-volumed
Version:	0.1.13
Release:	3
License:	GPL v3
Group:		Applications/System
Source0:	http://www.xfce.org/archive/src/apps/xfce4-volumed/0.1/%{name}-%{version}.tar.bz2
# Source0-md5:	03c0ee58aa0a080d35313ac517a975ea
URL:		https://launchpad.net/xfce4-volumed
BuildRequires:	glib2-devel >= 1:2.10.6
BuildRequires:	gstreamer-devel
BuildRequires:	gstreamer-plugins-base-devel
BuildRequires:	keybinder-devel
BuildRequires:	libnotify-devel
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	xfce4-dev-tools >= 4.8.0
BuildRequires:	xfconf-devel >= 4.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This daemon is responsible of making the volume up/down and mute
keys of the keyboard work automatically, and uses the XFCE mixer's
defined card and track for chosing which track to act on.
It also provides volume change / mute toggle notifications if
the notification server used supports x-canonical-icon-only and
x-canonical-synchronous notifications.

%description -l pl.UTF-8
Ten demon zapewnia automatyczne działanie klawiszy głośności na
klawiaturze przy użyciu miksera XFCE. Udostępnia również powiadomienia
jeśli serwer powiadomień obsługuje powiadomienia x-canonical-icon-only
i x-canonical-synchronous.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS
%attr(755,root,root) %{_bindir}/xfce4-volumed
/etc/xdg/autostart/xfce4-volumed.desktop
