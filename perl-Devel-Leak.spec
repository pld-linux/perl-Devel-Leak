%include	/usr/lib/rpm/macros.perl
Summary:	Devel-Leak perl module
Summary(pl):	Modu³ perla Devel-Leak
Name:		perl-Devel-Leak
Version:	0.02
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Devel/Devel-Leak-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
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
make OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT/%{perl_sitearch}/auto/Devel/Leak/*.so

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Devel/Leak
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz

%{perl_sitearch}/Devel/Leak.pm

%dir %{perl_sitearch}/auto/Devel/Leak
%{perl_sitearch}/auto/Devel/Leak/.packlist
%{perl_sitearch}/auto/Devel/Leak/Leak.bs
%attr(755,root,root) %{perl_sitearch}/auto/Devel/Leak/Leak.so

%{_mandir}/man3/*
