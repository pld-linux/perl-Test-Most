#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Test
%define		pnam	Most
Summary:	Test::Most - Most commonly needed test functions and features
Summary(pl.UTF-8):	Test::Most - najczęściej potrzebne funkcje testowe
Name:		perl-Test-Most
Version:	0.35
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	03dbabd34d6f40af8bd47f5fbb0c6989
URL:		http://search.cpan.org/dist/Test-Most/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Exception-Class >= 1.14
BuildRequires:	perl-Test-Deep >= 0.119
BuildRequires:	perl-Test-Differences >= 0.64
BuildRequires:	perl-Test-Exception >= 0.43
BuildRequires:	perl-Test-Harness >= 3.35
BuildRequires:	perl-Test-Simple >= 1.302047
BuildRequires:	perl-Test-Warn >= 0.30
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Test::Most exists to reduce boilerplate and to make your testing life
easier. We provide "one stop shopping" for most commonly used testing
modules. In fact, we often require the latest versions so that you get
bug fixes through Test::Most and don't have to keep upgrading these
modules separately.

This module provides you with the most commonly used testing
functions, along with automatically turning on strict and warning and
gives you a bit more fine-grained control over your test suite.

%description -l pl.UTF-8
Celem Test::Most jest zmniejszenie ilości ramowego kodu i ułatwienie
testowania. Moduł pozwala na jednoczesne włączenie najczęściej
używanych modułów testowych; zwykle wymagane są najnowsze wersje, aby
zapewnić poprawienie znanych błędów bez potrzeby uaktualniania modułów
osobno.

Test::Most dostarcza najczęściej używane funkcje testujące,
jednocześnie włączając tryb ścisły (strict) i ostrzeżenia, a także
pozwalając na elastyczną kontrolę zestawu testów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Test/Most.pm
%{perl_vendorlib}/Test/Most
%{_mandir}/man3/Test::Most.3pm*
%{_mandir}/man3/Test::Most::Exception.3pm*
