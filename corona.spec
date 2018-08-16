Summary:	Image input/output library
Summary(pl.UTF-8):	Biblioteka wejścia/wyjścia dla obrazów
Name:		corona
Version:	1.0.2
Release:	11
License:	zlib
Group:		Libraries
Source0:	http://downloads.sourceforge.net/corona/%{name}-%{version}.tar.gz
# Source0-md5:	29d1a7f1e2c85a83e9620496c62740ce
Patch0:		%{name}-system-gif.patch
Patch1:		%{name}-config.patch
Patch2:		%{name}-gcc43.patch
Patch3:		%{name}-libpng15.patch
Patch4:		giflib5.patch
URL:		http://corona.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dos2unix
BuildRequires:	giflib-devel >= 4.1.0
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	rpmbuild(macros) >= 1.565
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Corona is an image input/output library that can read, write, and
manipulate image files in just a few lines of code. It can write PNG
and TGA files, and read PNG, JPEG, PCX, BMP, TGA, and GIF. Corona was
designed to be easy to use, and exports a straightforward C++ API.
With just a few lines of C++, you can add image loading to your
application.

%description -l pl.UTF-8
Corona to biblioteka wejścia/wyjścia dla obrazów, potrafiąca czytać,
zapisywać i obrabiać pliki obrazów w zaledwie kilku liniach kodu.
Potrafi zapisywać pliki PNG i TGA, a czytać PNG, JPEG, PCX, BMP, TGA i
GIF. Została zaprojektowana jako łatwa w użyciu i eksportuje
bezpośrednie API C++. Za pomocą tylko kilku linii kodu C++ można dodać
wczytywanie obrazów do swojej aplikacji.

%package devel
Summary:	Header files for corona library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki corona
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	giflib-devel >= 4.1.0
Requires:	libjpeg-devel
Requires:	libpng-devel
Requires:	libstdc++-devel

%description devel
Header files for corona library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki corona.

%package static
Summary:	Static corona library
Summary(pl.UTF-8):	Statyczna biblioteka corona
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static corona library.

%description static -l pl.UTF-8
Statyczna biblioteka corona.

%prep
%setup -q
%undos src/*.cpp src/*.h
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc doc/{changelog.txt,faq.txt,license.txt,literature.txt,readme.txt}
%attr(755,root,root) %{_bindir}/corconvert
%attr(755,root,root) %{_libdir}/libcorona-*.so

%files devel
%defattr(644,root,root,755)
%doc doc/tutorial.txt
%attr(755,root,root) %{_bindir}/corona-config
%attr(755,root,root) %{_libdir}/libcorona.so
%{_libdir}/libcorona.la
%{_includedir}/corona.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libcorona.a
