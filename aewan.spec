Summary:	Aewan Ascii Art Editor
Summary(pl):	Edytor sztuki Ascii Aewan
Name:		aewan
Version:	0.9.3
Release:	1
License:	GPL
Group:		Applications/Editors
Source0:	http://dl.sourceforge.net/aewan/%{name}-%{version}.tar.gz
# Source0-md5:	5cff245a78f614a846c3328a9c2beb88
# Source0-size:	92160
Patch0:		%{name}-DESTDIR.patch
URL:		http://aewan.sourceforge.net/
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	ncurses-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Aewan is a multi-layered ascii-art/animation editor that produces both
stand-alone cat-able art files and an easy-to-parse format for
integration in your terminal applications.

%description -l pl
Aewan jest obs³uguj±cym wiele warstw edytorem sztuki ascii/animacji,
zdolnym do tworzenia zarówno samodzielnych cat-owalnych plików
ascii-art, jak tak¿e plików ³atwo parsowalnych dla integracji w
aplikacjach terminalowych.

%prep
%setup -q
%patch0 -p1

%build
CFLAGS="%{rpmcflags} -I%{_includedir}/ncurses"
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
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
