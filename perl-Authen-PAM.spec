%include	/usr/lib/rpm/macros.perl
%define	pdir	Authen
%define	pnam	PAM
Summary:	Authen-PAM perl module
Summary(pl):	Modu³ perla Authen-PAM
Name:		perl-Authen-PAM
Version:	0.12
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	pam-devel
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Authen-PAM provides a Perl interface to the PAM library.

%description -l pl
Authen-PAM umo¿liwia dostêp do biblioteki PAM.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

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
