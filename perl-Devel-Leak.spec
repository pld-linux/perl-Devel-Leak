#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Devel
%define	pnam	Leak
Summary:	Devel::Leak - utility for looking for Perl objects that are not reclaimed
Summary(pl):	Devel::Leak - narzêdzie do wyszukiwania niezwolnionych obiektów Perla 
Name:		perl-Devel-Leak
Version:	0.03
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9ee2cf88bd1dbc6091e38ef4597b54bb
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Devel::Leak is a utility for looking for Perl objects that are not
reclaimed.

%description -l pl
Devel::Leak jest narzêdziem s³u¿±cym do wyszukiwania niezwolnionych
obiektów Perla.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
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
