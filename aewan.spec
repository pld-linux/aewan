Summary:	Aewan Ascii Art Editor
Summary(pl.UTF-8):	Edytor sztuki Ascii Aewan
Name:		aewan
Version:	1.0.01
Release:	1
License:	GPL v2
Group:		Applications/Editors
Source0:	http://dl.sourceforge.net/aewan/%{name}-%{version}.tar.gz
# Source0-md5:	89545338d1eba311297b520f9dc1b976
URL:		http://aewan.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ncurses-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Aewan is a multi-layered ascii-art/animation editor that produces both
stand-alone cat-able art files and an easy-to-parse format for
integration in your terminal applications.

%description -l pl.UTF-8
Aewan jest obsługującym wiele warstw edytorem sztuki ascii/animacji,
zdolnym do tworzenia zarówno samodzielnych cat-owalnych plików
ascii-art, jak także plików łatwo parsowalnych dla integracji w
aplikacjach terminalowych.

%prep
%setup -q

%build
CFLAGS="%{rpmcflags} -I/usr/include/ncurses"
%{__aclocal}
%{__autoconf}
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
%doc CHANGELOG README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
