%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	DNS-Resolver-Programmable
Summary:	Net::DNS::Resolver::Programmable - programmable DNS resolver class for offline emulation of DNS
#Summary(pl.UTF-8):	
Name:		perl-Net-DNS-Resolver-Programmable
Version:	0.002.2
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8f3e5481e069c1657b8b4aefbfeb3549
URL:		http://search.cpan.org/dist/Net-DNS-Resolver-Programmable/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::DNS::Resolver::Programmable is a Net::DNS::Resolver descendant
class that allows a virtual DNS to be emulated instead of querying the real
DNS.  A set of static DNS records may be supplied, or arbitrary code may be
specified as a means for retrieving DNS records, or even generating them on the
fly.

The following constructor is provided:

The following instance methods of Net::DNS::Resolver are also supported by
Net::DNS::Resolver::Programmable:

Currently the following methods of Net::DNS::Resolver are not supported:
axfr, axfr_start, axfr_next, nameservers, port, srcport,
srcaddr, bgsend, bgread, bgisready, tsig, retrans, retry,
recurse, usevc, tcp_timeout, udp_timeout, persistent_tcp,
persistent_udp, igntc, dnssec, cdflag, udppacketsize.
The effects of using these on Net::DNS::Resolver::Programmable objects are
undefined.



# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES INSTALL README TODO
%{perl_vendorlib}/Net/DNS/Resolver/*.pm
%{_mandir}/man3/*
