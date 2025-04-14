
%define 	pypi_name	legacy_cgi
Summary:	Fork of the standard library cgi and cgitb modules removed in Python 3.13
Name:		python3-legacy-cgi
Version:	2.6.3
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/legacy_cgi/
Source0:	https://files.pythonhosted.org/packages/source/l/legacy_cgi/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	1c3a19d6391b0f87e5f52e4846a91a8a
URL:		https://github.com/jackrosenthal/legacy-cgi
BuildRequires:	python3-build
BuildRequires:	python3-hatchling
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.8
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fork of the standard library cgi and cgitb modules removed in Python
3.13.

%prep
%setup -q -n %{pypi_name}-%{version}

%{__sed} -i -e '1s,#!.*/usr/local/bin/python,#!%{__python3},' cgi.py

%build
%py3_build_pyproject

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/cgi.py
%{py3_sitescriptdir}/cgitb.py
%{py3_sitescriptdir}/__pycache__
%{py3_sitescriptdir}/%{pypi_name}-%{version}.dist-info
