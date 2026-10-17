Name:		python-sudsds
Version:	1.0.1
Release:	1
Summary:	SOAP client forked from suds for Datove schranky
License:	LGPL-3.0-or-later
Group:		Development/Python
URL:		https://labs.nic.cz/datove-schranky/
Source0:	https://labs.nic.cz/datove-schranky/sudsds-%{version}.tar.gz
# Upstream sudsds 1.0.1 is Python 2. The patch is a Python 3.15 port of that sdist.
Patch0:		sudsds-1.0.1-python315.patch
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python
BuildRequires:	python%{pyver}dist(setuptools)

%description
sudsds is a SOAP client library forked from suds, with the extra transport
features used by the Czech Datove schranky client. The import name is sudsds.

%files
%license LICENSE.txt
%doc README
%{py_puresitedir}/sudsds
%{py_puresitedir}/sudsds-%{version}-py%{pyver}.egg-info
%{_datadir}/sudsds
