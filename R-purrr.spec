#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-purrr
Version  : 0.3.4
Release  : 34
URL      : https://cran.r-project.org/src/contrib/purrr_0.3.4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/purrr_0.3.4.tar.gz
Summary  : Functional Programming Tools
Group    : Development/Tools
License  : GPL-3.0
Requires: R-purrr-lib = %{version}-%{release}
Requires: R-magrittr
Requires: R-rlang
BuildRequires : R-magrittr
BuildRequires : R-rlang
BuildRequires : buildreq-R

%description
toolkit for R.

%package lib
Summary: lib components for the R-purrr package.
Group: Libraries

%description lib
lib components for the R-purrr package.


%prep
%setup -q -c -n purrr
cd %{_builddir}/purrr

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589761597

%install
export SOURCE_DATE_EPOCH=1589761597
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
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
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library purrr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library purrr
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc purrr || :


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
/usr/lib64/R/library/purrr/help/figures/lifecycle-archived.svg
/usr/lib64/R/library/purrr/help/figures/lifecycle-defunct.svg
/usr/lib64/R/library/purrr/help/figures/lifecycle-deprecated.svg
/usr/lib64/R/library/purrr/help/figures/lifecycle-experimental.svg
/usr/lib64/R/library/purrr/help/figures/lifecycle-maturing.svg
/usr/lib64/R/library/purrr/help/figures/lifecycle-questioning.svg
/usr/lib64/R/library/purrr/help/figures/lifecycle-retired.svg
/usr/lib64/R/library/purrr/help/figures/lifecycle-soft-deprecated.svg
/usr/lib64/R/library/purrr/help/figures/lifecycle-stable.svg
/usr/lib64/R/library/purrr/help/figures/logo.png
/usr/lib64/R/library/purrr/help/paths.rds
/usr/lib64/R/library/purrr/help/purrr.rdb
/usr/lib64/R/library/purrr/help/purrr.rdx
/usr/lib64/R/library/purrr/html/00Index.html
/usr/lib64/R/library/purrr/html/R.css
/usr/lib64/R/library/purrr/tests/testthat.R
/usr/lib64/R/library/purrr/tests/testthat/compose-print.txt
/usr/lib64/R/library/purrr/tests/testthat/helper-conditions.R
/usr/lib64/R/library/purrr/tests/testthat/helper-map.R
/usr/lib64/R/library/purrr/tests/testthat/setup.R
/usr/lib64/R/library/purrr/tests/testthat/test-along.R
/usr/lib64/R/library/purrr/tests/testthat/test-arrays.R
/usr/lib64/R/library/purrr/tests/testthat/test-as-mapper.R
/usr/lib64/R/library/purrr/tests/testthat/test-chuck.R
/usr/lib64/R/library/purrr/tests/testthat/test-coerce.R
/usr/lib64/R/library/purrr/tests/testthat/test-compose.R
/usr/lib64/R/library/purrr/tests/testthat/test-composition.R
/usr/lib64/R/library/purrr/tests/testthat/test-conditions.R
/usr/lib64/R/library/purrr/tests/testthat/test-cross.R
/usr/lib64/R/library/purrr/tests/testthat/test-depth.R
/usr/lib64/R/library/purrr/tests/testthat/test-detect.R
/usr/lib64/R/library/purrr/tests/testthat/test-every-some-none.R
/usr/lib64/R/library/purrr/tests/testthat/test-flatten.R
/usr/lib64/R/library/purrr/tests/testthat/test-head-tail.R
/usr/lib64/R/library/purrr/tests/testthat/test-imap.R
/usr/lib64/R/library/purrr/tests/testthat/test-list-modify-update.R
/usr/lib64/R/library/purrr/tests/testthat/test-lmap.R
/usr/lib64/R/library/purrr/tests/testthat/test-map.R
/usr/lib64/R/library/purrr/tests/testthat/test-map2.R
/usr/lib64/R/library/purrr/tests/testthat/test-map_n.R
/usr/lib64/R/library/purrr/tests/testthat/test-modify.R
/usr/lib64/R/library/purrr/tests/testthat/test-negate.R
/usr/lib64/R/library/purrr/tests/testthat/test-output.R
/usr/lib64/R/library/purrr/tests/testthat/test-partial-print.txt
/usr/lib64/R/library/purrr/tests/testthat/test-partial.R
/usr/lib64/R/library/purrr/tests/testthat/test-pluck.R
/usr/lib64/R/library/purrr/tests/testthat/test-predicates.R
/usr/lib64/R/library/purrr/tests/testthat/test-prepend.R
/usr/lib64/R/library/purrr/tests/testthat/test-rate-print.txt
/usr/lib64/R/library/purrr/tests/testthat/test-rate.R
/usr/lib64/R/library/purrr/tests/testthat/test-recycle_args.R
/usr/lib64/R/library/purrr/tests/testthat/test-reduce.R
/usr/lib64/R/library/purrr/tests/testthat/test-rerun.R
/usr/lib64/R/library/purrr/tests/testthat/test-retired-invoke.R
/usr/lib64/R/library/purrr/tests/testthat/test-simplify.R
/usr/lib64/R/library/purrr/tests/testthat/test-splice.R
/usr/lib64/R/library/purrr/tests/testthat/test-transpose.R
/usr/lib64/R/library/purrr/tests/testthat/test-utils.R
/usr/lib64/R/library/purrr/tests/testthat/test-when.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/purrr/libs/purrr.so
