%define upstream_name    Net-HTTP
%define upstream_version 6.01

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    7

Summary:    Non-blocking HTTP client
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Compress::Raw::Zlib)
BuildRequires: perl(IO::Compress::Gzip)
BuildRequires: perl(IO::Select)
BuildRequires: perl(IO::Socket::INET)
BuildRequires: perl-devel
BuildArch: noarch

%description
The 'Net::HTTP' class is a low-level HTTP client. An instance of the
'Net::HTTP' class represents a connection to an HTTP server. The HTTP
protocol is described in RFC 2616. The 'Net::HTTP' class supports
'HTTP/1.0' and 'HTTP/1.1'.

'Net::HTTP' is a sub-class of 'IO::Socket::INET'. You can mix the methods
described below with reading and writing from the socket directly. This is
not necessary a good idea, unless you know what you are doing.

The following methods are provided (in addition to those of
'IO::Socket::INET'):

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 6.10.0-4mdv2012.0
+ Revision: 765526
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 6.10.0-3
+ Revision: 764048
- rebuilt for perl-5.14.x

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 6.10.0-2
+ Revision: 763095
- rebuild

* Tue May 03 2011 Guillaume Rousse <guillomovitch@mandriva.org> 6.10.0-1
+ Revision: 664979
- import perl-Net-HTTP

