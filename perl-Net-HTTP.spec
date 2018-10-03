%define modname	Net-HTTP
%define modver 6.18

Summary:	Non-blocking HTTP client
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Net/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Compress::Raw::Zlib)
BuildRequires:	perl(URI)
BuildRequires:	perl(IO::Compress::Gzip)
BuildRequires:	perl(IO::Select)
BuildRequires:	perl(IO::Socket::INET)
BuildRequires:	perl-devel
Requires:       perl(IO::Socket::SSL)

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
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml
%{perl_vendorlib}/*
%{_mandir}/man3/*
