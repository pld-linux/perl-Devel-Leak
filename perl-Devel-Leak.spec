%define	pdir	Devel
%define	pnam	Leak
%include	/usr/lib/rpm/macros.perl
Summary:	Devel-Leak perl module
Summary(pl):	Modu³ perla Devel-Leak
Name:		perl-Devel-Leak
Version:	0.02
Release:	4

License:	GPL
Group:		Development/Languages/Perl
Group(cs):	Vývojové prostøedky/Programovací jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	³«È¯/¸À¸ì/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	òÁÚÒÁÂÏÔËÁ/ñÚÙËÉ/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Devel-Leak - Utility for looking for perl objects that are not
reclaimed.

%description -l pl
Modu³ perla Devel-Leak.

%prep
%setup -q -n Devel-Leak-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitearch}/Devel/Leak.pm
%dir %{perl_sitearch}/auto/Devel/Leak
%{perl_sitearch}/auto/Devel/Leak/Leak.bs
%attr(755,root,root) %{perl_sitearch}/auto/Devel/Leak/Leak.so
%{_mandir}/man3/*
