%define upstream_name    Log-Contextual
%define upstream_version 0.00304

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Super simple logger made for playing with Log::Contextual
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Log/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Data::Dumper::Concise)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module is a simple interface to extensible logging. It is bundled with
a really basic logger, the Log::Contextual::SimpleLogger manpage, but in
general you should use a real logger instead of that. For something more
serious but not overly complicated, try the Log::Dispatchouli manpage (see
the /SYNOPSIS manpage for example.)

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
%doc Changes META.yml
%{_mandir}/man3/*
%perl_vendorlib/*


