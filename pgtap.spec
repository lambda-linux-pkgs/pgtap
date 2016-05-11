%define _buildid .1

%global pg92nvr pgtap92-%{version}-%{release}
%global pg92builddir %{_builddir}/%{pg92nvr}

%global pg93nvr pgtap93-%{version}-%{release}
%global pg93builddir %{_builddir}/%{pg93nvr}

%global pg94nvr pgtap94-%{version}-%{release}
%global pg94builddir %{_builddir}/%{pg94nvr}

Summary:	Unit testing suite for PostgreSQL
Name:		pgtap
Version:	0.95.0
Release:	1%{?_buildid}%{?dist}
Group:		Applications/Databases
License:	PostgreSQL
URL:		http://pgtap.org/
Source0:	http://master.pgxn.org/dist/pgtap/%{version}/pgtap-%{version}.zip
BuildArch:      noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:  perl-TAP-Parser-SourceHandler-pgTAP >= 3.30

# Lambda Linux patches
Patch1001: 1001-Remove-default-definition-of-PG_CONFIG.patch

%description
For package support, please visit
https://github.com/lambda-linux-pkgs/%{name}/issues

pgTAP is a unit testing framework for PostgreSQL written in PL/pgSQL and
PL/SQL. It includes a comprehensive collection of TAP-emitting assertion
functions, as well as the ability to integrate with other TAP-emitting test
frameworks. It can also be used in the xUnit testing style.

%package -n pgtap92
Summary:	Unit testing suite for PostgreSQL
Requires:       postgresql92-server, perl-Test-Harness >= 3.0
Requires:       perl-TAP-Parser-SourceHandler-pgTAP >= 3.30
BuildRequires:  postgresql92-devel

%description -n pgtap92
For package support, please visit
https://github.com/lambda-linux-pkgs/%{name}/issues

pgTAP is a unit testing framework for PostgreSQL written in PL/pgSQL and
PL/SQL. It includes a comprehensive collection of TAP-emitting assertion
functions, as well as the ability to integrate with other TAP-emitting test
frameworks. It can also be used in the xUnit testing style.

This package is meant to be used with PostgreSQL 9.2

%package -n pgtap93
Summary:	Unit testing suite for PostgreSQL
Requires:       postgresql93-server, perl-Test-Harness >= 3.0
Requires:       perl-TAP-Parser-SourceHandler-pgTAP >= 3.30
BuildRequires:  postgresql93-devel

%description -n pgtap93
For package support, please visit
https://github.com/lambda-linux-pkgs/%{name}/issues

pgTAP is a unit testing framework for PostgreSQL written in PL/pgSQL and
PL/SQL. It includes a comprehensive collection of TAP-emitting assertion
functions, as well as the ability to integrate with other TAP-emitting test
frameworks. It can also be used in the xUnit testing style.

This package is meant to be used with PostgreSQL 9.3

%package -n pgtap94
Summary:	Unit testing suite for PostgreSQL
Requires:       postgresql94-server, perl-Test-Harness >= 3.0
Requires:       perl-TAP-Parser-SourceHandler-pgTAP >= 3.30
BuildRequires:  postgresql94-devel

%description -n pgtap94
For package support, please visit
https://github.com/lambda-linux-pkgs/%{name}/issues

pgTAP is a unit testing framework for PostgreSQL written in PL/pgSQL and
PL/SQL. It includes a comprehensive collection of TAP-emitting assertion
functions, as well as the ability to integrate with other TAP-emitting test
frameworks. It can also be used in the xUnit testing style.

This package is meant to be used with PostgreSQL 9.4

%prep
%setup -q

# Lambda Linux patches
%patch1001 -p1

%build
rm -rf %{pg92builddir}
mkdir -p %{pg92builddir}
cp -a * %{pg92builddir}
pushd %{pg92builddir}
env PG_CONFIG=/usr/bin/pg_config92 make
popd

rm -rf %{pg93builddir}
mkdir -p %{pg93builddir}
cp -a * %{pg93builddir}
pushd %{pg93builddir}
env PG_CONFIG=/usr/bin/pg_config93 make
popd

rm -rf %{pg94builddir}
mkdir -p %{pg94builddir}
cp -a * %{pg94builddir}
pushd %{pg94builddir}
env PG_CONFIG=/usr/bin/pg_config94 make
popd

%install
%{__rm} -rf %{buildroot}

pushd %{pg92builddir}
env PG_CONFIG=/usr/bin/pg_config92 make install DESTDIR=%{buildroot}
popd

pushd %{pg93builddir}
env PG_CONFIG=/usr/bin/pg_config93 make install DESTDIR=%{buildroot}
popd

pushd %{pg94builddir}
env PG_CONFIG=/usr/bin/pg_config94 make install DESTDIR=%{buildroot}
popd

%clean
%{__rm} -rf %{buildroot}
%{__rm} -rf %{pg92builddir}
%{__rm} -rf %{pg93builddir}
%{__rm} -rf %{pg94builddir}

%files -n pgtap92
%defattr(-,root,root,-)
%{_datadir}/pgsql92/extension/pgtap*
%{_defaultdocdir}/pgsql/extension/pgtap.mmd

%files -n pgtap93
%defattr(-,root,root,-)
%{_datadir}/pgsql93/extension/pgtap*
%{_defaultdocdir}/pgsql/extension/pgtap.mmd

%files -n pgtap94
%defattr(-,root,root,-)
%{_datadir}/pgsql94/extension/pgtap*
%{_defaultdocdir}/pgsql/extension/pgtap.mmd

%changelog
* Tue Jun 09 2015 Rajiv M Ranganath <rajiv.ranganath@atihita.com> 0.95.0-1
- Adapt for AL/LL
- Add package support URL
- Update spec file for AL/LL
- Add `1001-Remove-default-definition-of-PG_CONFIG.patch`
- Import `pgtap-0.95.0.zip`
- Import spec file

* Mon Jan 28 2013 David Wheeler <david@justatheory.com> 0.93.0
- Upgraded to pgTAP 0.93.0

* Tue Jan 15 2013 David E. Wheeler <david@justatheory.com> 0.92.0-1
- Upgraded to pgTAP 0.92.0

* Tue Aug 23 2011 David Wheeler <david@justatheory.com> 0.91.0
- Removed USE_PGXS from Makefile; it has not been supported in some time.
- Removed TAPSCHEMA from Makefile; use PGOPTIONS=--search_path=tap with
  psql instead.

* Tue Feb 01 2011 David Wheeler <david@justatheory.com> 0.25.0
- Removed pg_prove and pg_tapgen, which are now distributed via CPAN.

* Sun Mar 01 2010 Darrell Fuhriman <darrell@renewfund.com> 0.24-2
- Make install work where the pgtap.so library is needed.

* Sun Dec 27 2009 David Wheeler <david@justatheory.com> 0.24-1
- Updated Source URL to a more predictable format.

* Mon Aug 24 2009 David Fetter <david.fetter@pgexperts.com> 0.23-1
- Got corrected .spec from Devrim GUNDUZ <devrim@gunduz.org>
- Bumped version to 0.23.

* Wed Aug 19 2009 Darrell Fuhriman <darrell@projectdx.com> 0.22-1
- initial RPM
