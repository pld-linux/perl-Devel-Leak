#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Devel
%define		pnam	Leak
Summary:	Devel::Leak - utility for looking for Perl objects that are not reclaimed
Summary(pl.UTF-8):	Devel::Leak - narzędzie do wyszukiwania niezwolnionych obiektów Perla 
Name:		perl-Devel-Leak
Version:	0.03
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Devel/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9ee2cf88bd1dbc6091e38ef4597b54bb
URL:		http://search.cpan.org/dist/Devel-Leak/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Devel::Leak is a utility for looking for Perl objects that are not
reclaimed.

%description -l pl.UTF-8
Devel::Leak jest narzędziem służącym do wyszukiwania niezwolnionych
obiektów Perla.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorarch}/Devel/Leak.pm
%dir %{perl_vendorarch}/auto/Devel/Leak
%{perl_vendorarch}/auto/Devel/Leak/Leak.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Devel/Leak/Leak.so
%{_mandir}/man3/*
