%define upstream_name    Net-HTTP
%define upstream_version 6.01

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 4

Summary:    Non-blocking HTTP client
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Compress::Raw::Zlib)
BuildRequires: perl(IO::Compress::Gzip)
BuildRequires: perl(IO::Select)
BuildRequires: perl(IO::Socket::INET)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


