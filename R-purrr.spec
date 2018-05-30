#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-purrr
Version  : 0.2.5
Release  : 10
URL      : https://cran.r-project.org/src/contrib/purrr_0.2.5.tar.gz
Source0  : https://cran.r-project.org/src/contrib/purrr_0.2.5.tar.gz
Summary  : Functional Programming Tools
Group    : Development/Tools
License  : GPL-3.0
Requires: R-purrr-lib
Requires: R-tibble
BuildRequires : R-tibble
BuildRequires : clr-R-helpers

%description
purrr <img src="man/figures/logo.png" align="right" />
======================================================

%package lib
Summary: lib components for the R-purrr package.
Group: Libraries

%description lib
lib components for the R-purrr package.


%prep
%setup -q -c -n purrr

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1527657318

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1527657318
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library purrr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library purrr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library purrr
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library purrr|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/purrr/DESCRIPTION
/usr/lib64/R/library/purrr/INDEX
/usr/lib64/R/library/purrr/LICENSE
/usr/lib64/R/library/purrr/Meta/Rd.rds
/usr/lib64/R/library/purrr/Meta/features.rds
/usr/lib64/R/library/purrr/Meta/hsearch.rds
/usr/lib64/R/library/purrr/Meta/links.rds
/usr/lib64/R/library/purrr/Meta/nsInfo.rds
/usr/lib64/R/library/purrr/Meta/package.rds
/usr/lib64/R/library/purrr/Meta/vignette.rds
/usr/lib64/R/library/purrr/NAMESPACE
/usr/lib64/R/library/purrr/NEWS.md
/usr/lib64/R/library/purrr/R/purrr
/usr/lib64/R/library/purrr/R/purrr.rdb
/usr/lib64/R/library/purrr/R/purrr.rdx
/usr/lib64/R/library/purrr/doc/index.html
/usr/lib64/R/library/purrr/doc/other-langs.Rmd
/usr/lib64/R/library/purrr/doc/other-langs.html
/usr/lib64/R/library/purrr/help/AnIndex
/usr/lib64/R/library/purrr/help/aliases.rds
/usr/lib64/R/library/purrr/help/figures/logo.png
/usr/lib64/R/library/purrr/help/paths.rds
/usr/lib64/R/library/purrr/help/purrr.rdb
/usr/lib64/R/library/purrr/help/purrr.rdx
/usr/lib64/R/library/purrr/html/00Index.html
/usr/lib64/R/library/purrr/html/R.css
/usr/lib64/R/library/purrr/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/purrr/libs/purrr.so
/usr/lib64/R/library/purrr/libs/purrr.so.avx2
/usr/lib64/R/library/purrr/libs/purrr.so.avx512
