#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : antlr4-python3-runtime
Version  : 4.8
Release  : 2
URL      : https://files.pythonhosted.org/packages/56/02/789a0bddf9c9b31b14c3e79ec22b9656185a803dc31c15f006f9855ece0d/antlr4-python3-runtime-4.8.tar.gz
Source0  : https://files.pythonhosted.org/packages/56/02/789a0bddf9c9b31b14c3e79ec22b9656185a803dc31c15f006f9855ece0d/antlr4-python3-runtime-4.8.tar.gz
Summary  : ANTLR 4.8 runtime for Python 3.7
Group    : Development/Tools
License  : BSD-3-Clause
Requires: antlr4-python3-runtime-python = %{version}-%{release}
Requires: antlr4-python3-runtime-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
This is the Python 3.4 runtime for ANTLR.
Visit the ANTLR web sites for more information:
http://www.antlr.org
https://raw.githubusercontent.com/antlr/antlr4/master/doc/python-target.md

%package python
Summary: python components for the antlr4-python3-runtime package.
Group: Default
Requires: antlr4-python3-runtime-python3 = %{version}-%{release}

%description python
python components for the antlr4-python3-runtime package.


%package python3
Summary: python3 components for the antlr4-python3-runtime package.
Group: Default
Requires: python3-core
Provides: pypi(antlr4_python3_runtime)

%description python3
python3 components for the antlr4-python3-runtime package.


%prep
%setup -q -n antlr4-python3-runtime-4.8
cd %{_builddir}/antlr4-python3-runtime-4.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1588632910
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
