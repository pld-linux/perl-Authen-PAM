%include	/usr/lib/rpm/macros.perl
Summary:	Authen-PAM perl module
Summary(pl):	Modu³ perla Authen-PAM
Name:		perl-Authen-PAM
Version:	0.11
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Authen/Authen-PAM-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	pam-devel
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Authen-PAM provides a Perl interface to the PAM library.

%description -l pl
Authen-PAM umo¿liwia dostêp do biblioteki PAM.

%prep
%setup -q -n Authen-PAM-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{?debug:-O0 -g}%{!?debug:$RPM_OPT_FLAGS}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitearch}/Authen/PAM.pm
%dir %{perl_sitearch}/auto/Authen/PAM
%attr(755,root,root) %{perl_sitearch}/auto/Authen/PAM/PAM.so
%{_mandir}/man3/*
