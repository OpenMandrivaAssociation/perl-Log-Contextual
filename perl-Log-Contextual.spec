%define upstream_name    Log-Contextual
%define upstream_version 0.00304

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Super simple logger made for playing with Log::Contextual
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Log/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Data::Dumper::Concise)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildArch:	noarch

%description
This module is a simple interface to extensible logging. It is bundled with
a really basic logger, the Log::Contextual::SimpleLogger manpage, but in
general you should use a real logger instead of that. For something more
serious but not overly complicated, try the Log::Dispatchouli manpage (see
the /SYNOPSIS manpage for example.)

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.3.40-2mdv2011.0
+ Revision: 655601
- rebuild for updated spec-helper

* Wed Aug 11 2010 Shlomi Fish <shlomif@mandriva.org> 0.3.40-1mdv2011.0
+ Revision: 569118
- Upgraded to 0.00304
- import perl-Log-Contextual


* Tue Jul 27 2010 cpan2dist 0.00303-1mdv
- initial mdv release, generated with cpan2dist
