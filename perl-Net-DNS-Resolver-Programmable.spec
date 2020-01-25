%define	pdir	Net
%define	pnam	DNS-Resolver-Programmable
Summary:	Net::DNS::Resolver::Programmable - programmable DNS resolver class for offline emulation of DNS
Summary(pl.UTF-8):	Net::DNS::Resolver::Programmable - klasa programowalnego resolvera DNS do emulacji DNS-a offline
Name:		perl-Net-DNS-Resolver-Programmable
Version:	0.009
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f42a7e7984c258db0ef127b217a2bcb4
URL:		http://search.cpan.org/dist/Net-DNS-Resolver-Programmable/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-version
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Net-DNS >= 0.59-2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::DNS::Resolver::Programmable is a Net::DNS::Resolver descendant
class that allows a virtual DNS to be emulated instead of querying the
real DNS. A set of static DNS records may be supplied, or arbitrary
code may be specified as a means for retrieving DNS records, or even
generating them on the fly.

%description -l pl.UTF-8
Net::DNS::Resolver::Programmable to klasa potomna klasy
Net::DNS::Resolver pozwalająca na emulowanie wirtualnego DNS-a zamiast
odpytywania rzeczywistego. Można przekazać zbiór statycznych rekordów
DNS, przekazać dowolny kod do odtwarzania rekordów DNS, a nawet
generować je w locie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES INSTALL README TODO
%{perl_vendorlib}/Net/DNS/Resolver/*.pm
%{_mandir}/man3/*
