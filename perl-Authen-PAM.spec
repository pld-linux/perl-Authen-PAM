#
# Conditional build:
%bcond_with	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Authen
%define	pnam	PAM
Summary:	Authen::PAM - Perl interface to PAM library
Summary(pl):	Authen::PAM - interfejs perlowy do biblioteki PAM
Name:		perl-Authen-PAM
Version:	0.14
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Vendor:		Nikolay Pelov <pelov@cs.kuleuven.ac.be>
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	cc17168f6645022ff52b594ef96940ab
URL:		http://www.cs.kuleuven.ac.be/~pelov/pam/
BuildRequires:	pam-devel
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Authen::PAM module provides a Perl interface to the PAM library.

%description -l pl
Modu� Authen::PAM umo�liwia dost�p z Perla do biblioteki PAM.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

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
