%include	/usr/lib/rpm/macros.perl
%define	pdir	Authen
%define	pnam	PAM
Summary:	Authen::PAM perl module
Summary(pl):	Modu³ perla Authen::PAM
Name:		perl-Authen-PAM
Version:	0.13
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	pam-devel
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Authen::PAM provides a Perl interface to the PAM library.

%description -l pl
Authen::PAM umo¿liwia dostêp do biblioteki PAM.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitearch}/Authen/*
%{perl_sitearch}/auto/Authen/PAM
%{_mandir}/man3/*
