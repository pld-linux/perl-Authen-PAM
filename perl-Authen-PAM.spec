#
# Conditional build:
%bcond_with	tests	# perform "make test" (interactive)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Authen
%define		pnam	PAM
Summary:	Authen::PAM - Perl interface to PAM library
Summary(pl.UTF-8):	Authen::PAM - interfejs perlowy do biblioteki PAM
Name:		perl-Authen-PAM
Version:	0.16
Release:	16
# same as perl
License:	GPL v1+ or Artistic
Vendor:		Nikolay Pelov <pelov@cs.kuleuven.ac.be>
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7278471dfa694d9ef312bc92d7099af2
URL:		http://www.cs.kuleuven.ac.be/~pelov/pam/
BuildRequires:	pam-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Authen::PAM module provides a Perl interface to the PAM library.

%description -l pl.UTF-8
Moduł Authen::PAM umożliwia dostęp z Perla do biblioteki PAM.

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
%doc Changes README
%{perl_vendorarch}/Authen/*.pm
%dir %{perl_vendorarch}/auto/Authen/PAM
%attr(755,root,root) %{perl_vendorarch}/auto/Authen/PAM/PAM.so
%{_mandir}/man3/*
