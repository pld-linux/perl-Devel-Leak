%include	/usr/lib/rpm/macros.perl
%define	pdir	Devel
%define	pnam	Leak
Summary:	Devel::Leak perl module
Summary(pl):	Modu³ perla Devel::Leak
Name:		perl-Devel-Leak
Version:	0.03
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9ee2cf88bd1dbc6091e38ef4597b54bb
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Devel::Leak - Utility for looking for perl objects that are not
reclaimed.

%description -l pl
Modu³ perla Devel::Leak.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

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
