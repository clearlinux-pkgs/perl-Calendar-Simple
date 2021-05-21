#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Calendar-Simple
Version  : 2.0.1
Release  : 19
URL      : https://cpan.metacpan.org/authors/id/D/DA/DAVECROSS/Calendar-Simple-v2.0.1.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DA/DAVECROSS/Calendar-Simple-v2.0.1.tar.gz
Summary  : 'Perl extension to create simple calendars'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Calendar-Simple-bin = %{version}-%{release}
Requires: perl-Calendar-Simple-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Calendar::Simple
----------------
This is a very simple module that models a calendar month.

%package bin
Summary: bin components for the perl-Calendar-Simple package.
Group: Binaries

%description bin
bin components for the perl-Calendar-Simple package.


%package dev
Summary: dev components for the perl-Calendar-Simple package.
Group: Development
Requires: perl-Calendar-Simple-bin = %{version}-%{release}
Provides: perl-Calendar-Simple-devel = %{version}-%{release}
Requires: perl-Calendar-Simple = %{version}-%{release}

%description dev
dev components for the perl-Calendar-Simple package.


%package perl
Summary: perl components for the perl-Calendar-Simple package.
Group: Default
Requires: perl-Calendar-Simple = %{version}-%{release}

%description perl
perl components for the perl-Calendar-Simple package.


%prep
%setup -q -n Calendar-Simple-v2.0.1
cd %{_builddir}/Calendar-Simple-v2.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pcal

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Calendar::Simple.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Calendar/Simple.pm
