#
# Conditional build:
# _with_tests - perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Authen
%define	pnam	PAM
Summary:	Authen::PAM Perl module
Summary(cs):	Modul Authen::PAM pro Perl
Summary(da):	Perlmodul Authen::PAM
Summary(de):	Authen::PAM Perl Modul
Summary(es):	Módulo de Perl Authen::PAM
Summary(fr):	Module Perl Authen::PAM
Summary(it):	Modulo di Perl Authen::PAM
Summary(ja):	Authen::PAM Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Authen::PAM ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Authen::PAM
Summary(pl):	Modu³ Perla Authen::PAM
Summary(pt):	Módulo de Perl Authen::PAM
Summary(pt_BR):	Módulo Perl Authen::PAM
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Authen::PAM
Summary(sv):	Authen::PAM Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Authen::PAM
Summary(zh_CN):	Authen::PAM Perl Ä£¿é
Name:		perl-Authen-PAM
Version:	0.14
Release:	3
Vendor:		Nikolay Pelov <pelov@cs.kuleuven.ac.be>
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
URL:		http://www.cs.kuleuven.ac.be/~pelov/pam/
BuildRequires:	pam-devel
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Authen::PAM provides a Perl interface to the PAM library.

%description -l pl
Authen::PAM umo¿liwia dostêp do biblioteki PAM.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make} OPTIMIZE="%{rpmcflags}"

%{?_with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Authen/*.pm
%dir %{perl_vendorarch}/auto/Authen/PAM
%{perl_vendorarch}/auto/Authen/PAM/PAM.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Authen/PAM/PAM.so
%{_mandir}/man3/*
