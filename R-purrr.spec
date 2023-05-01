#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-purrr
Version  : 1.0.1
Release  : 55
URL      : https://cran.r-project.org/src/contrib/purrr_1.0.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/purrr_1.0.1.tar.gz
Summary  : Functional Programming Tools
Group    : Development/Tools
License  : MIT
Requires: R-purrr-lib = %{version}-%{release}
Requires: R-cli
Requires: R-lifecycle
Requires: R-magrittr
Requires: R-rlang
Requires: R-vctrs
BuildRequires : R-cli
BuildRequires : R-lifecycle
BuildRequires : R-lubridate
BuildRequires : R-magrittr
BuildRequires : R-rlang
BuildRequires : R-vctrs
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# purrr <img src="man/figures/logo.png" align="right" />
<!-- badges: start -->
[![CRAN_Status_Badge](https://www.r-pkg.org/badges/version/purrr)](https://cran.r-project.org/package=purrr)
[![Codecov test
coverage](https://codecov.io/gh/tidyverse/purrr/branch/master/graph/badge.svg)](https://app.codecov.io/gh/tidyverse/purrr?branch=master)
[![R build
status](https://github.com/tidyverse/purrr/workflows/R-CMD-check/badge.svg)](https://github.com/tidyverse/purrr/actions)
<!-- badges: end -->

%package lib
Summary: lib components for the R-purrr package.
Group: Libraries

%description lib
lib components for the R-purrr package.


%prep
%setup -q -n purrr
cd %{_builddir}/purrr

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1673456553

%install
export SOURCE_DATE_EPOCH=1673456553
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
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


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
/usr/lib64/R/library/purrr/doc/base.R
/usr/lib64/R/library/purrr/doc/base.Rmd
/usr/lib64/R/library/purrr/doc/base.html
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
/usr/lib64/R/library/purrr/help/figures/lifecycle-soft-deprecated.svg
/usr/lib64/R/library/purrr/help/figures/lifecycle-stable.svg
/usr/lib64/R/library/purrr/help/figures/lifecycle-superseded.svg
/usr/lib64/R/library/purrr/help/figures/logo.png
/usr/lib64/R/library/purrr/help/paths.rds
/usr/lib64/R/library/purrr/help/purrr.rdb
/usr/lib64/R/library/purrr/help/purrr.rdx
/usr/lib64/R/library/purrr/html/00Index.html
/usr/lib64/R/library/purrr/html/R.css
/usr/lib64/R/library/purrr/tests/testthat.R
/usr/lib64/R/library/purrr/tests/testthat/_snaps/adverb-auto-browse.md
/usr/lib64/R/library/purrr/tests/testthat/_snaps/adverb-compose.md
/usr/lib64/R/library/purrr/tests/testthat/_snaps/adverb-insistently.md
/usr/lib64/R/library/purrr/tests/testthat/_snaps/adverb-partial.md
/usr/lib64/R/library/purrr/tests/testthat/_snaps/adverb-slowly.md
/usr/lib64/R/library/purrr/tests/testthat/_snaps/arrays.md
/usr/lib64/R/library/purrr/tests/testthat/_snaps/coerce.md
/usr/lib64/R/library/purrr/tests/testthat/_snaps/conditions.md
/usr/lib64/R/library/purrr/tests/testthat/_snaps/deprec-along.md
/usr/lib64/R/library/purrr/tests/testthat/_snaps/deprec-cross.md
/usr/lib64/R/library/purrr/tests/testthat/_snaps/deprec-invoke.md
/usr/lib64/R/library/purrr/tests/testthat/_snaps/deprec-lift.md
/usr/lib64/R/library/purrr/tests/testthat/_snaps/deprec-map.md
/usr/lib64/R/library/purrr/tests/testthat/_snaps/deprec-prepend.md
/usr/lib64/R/library/purrr/tests/testthat/_snaps/deprec-rerun.md
/usr/lib64/R/library/purrr/tests/testthat/_snaps/deprec-splice.md
/usr/lib64/R/library/purrr/tests/testthat/_snaps/deprec-utils.md
/usr/lib64/R/library/purrr/tests/testthat/_snaps/deprec-when.md
/usr/lib64/R/library/purrr/tests/testthat/_snaps/detect.md
/usr/lib64/R/library/purrr/tests/testthat/_snaps/head-tail.md
/usr/lib64/R/library/purrr/tests/testthat/_snaps/keep.md
/usr/lib64/R/library/purrr/tests/testthat/_snaps/list-combine.md
/usr/lib64/R/library/purrr/tests/testthat/_snaps/list-flatten.md
/usr/lib64/R/library/purrr/tests/testthat/_snaps/list-modify.md
/usr/lib64/R/library/purrr/tests/testthat/_snaps/list-simplify.md
/usr/lib64/R/library/purrr/tests/testthat/_snaps/list-transpose.md
/usr/lib64/R/library/purrr/tests/testthat/_snaps/lmap.md
/usr/lib64/R/library/purrr/tests/testthat/_snaps/map-depth.md
/usr/lib64/R/library/purrr/tests/testthat/_snaps/map-if-at.md
/usr/lib64/R/library/purrr/tests/testthat/_snaps/map-raw.md
/usr/lib64/R/library/purrr/tests/testthat/_snaps/map.md
/usr/lib64/R/library/purrr/tests/testthat/_snaps/map2.md
/usr/lib64/R/library/purrr/tests/testthat/_snaps/modify-tree.md
/usr/lib64/R/library/purrr/tests/testthat/_snaps/modify.md
/usr/lib64/R/library/purrr/tests/testthat/_snaps/pluck-assign.md
/usr/lib64/R/library/purrr/tests/testthat/_snaps/pluck-depth.md
/usr/lib64/R/library/purrr/tests/testthat/_snaps/pluck.md
/usr/lib64/R/library/purrr/tests/testthat/_snaps/pmap.md
/usr/lib64/R/library/purrr/tests/testthat/_snaps/rate.md
/usr/lib64/R/library/purrr/tests/testthat/_snaps/reduce.md
/usr/lib64/R/library/purrr/tests/testthat/_snaps/superseded-flatten.md
/usr/lib64/R/library/purrr/tests/testthat/_snaps/superseded-transpose.md
/usr/lib64/R/library/purrr/tests/testthat/_snaps/utils.md
/usr/lib64/R/library/purrr/tests/testthat/helper-map.R
/usr/lib64/R/library/purrr/tests/testthat/helper.R
/usr/lib64/R/library/purrr/tests/testthat/setup.R
/usr/lib64/R/library/purrr/tests/testthat/test-adverb-auto-browse.R
/usr/lib64/R/library/purrr/tests/testthat/test-adverb-compose.R
/usr/lib64/R/library/purrr/tests/testthat/test-adverb-insistently.R
/usr/lib64/R/library/purrr/tests/testthat/test-adverb-negate.R
/usr/lib64/R/library/purrr/tests/testthat/test-adverb-partial.R
/usr/lib64/R/library/purrr/tests/testthat/test-adverb-possibly.R
/usr/lib64/R/library/purrr/tests/testthat/test-adverb-quietly.R
/usr/lib64/R/library/purrr/tests/testthat/test-adverb-safely.R
/usr/lib64/R/library/purrr/tests/testthat/test-adverb-slowly.R
/usr/lib64/R/library/purrr/tests/testthat/test-arrays.R
/usr/lib64/R/library/purrr/tests/testthat/test-coerce.R
/usr/lib64/R/library/purrr/tests/testthat/test-conditions.R
/usr/lib64/R/library/purrr/tests/testthat/test-deprec-along.R
/usr/lib64/R/library/purrr/tests/testthat/test-deprec-cross.R
/usr/lib64/R/library/purrr/tests/testthat/test-deprec-invoke.R
/usr/lib64/R/library/purrr/tests/testthat/test-deprec-lift.R
/usr/lib64/R/library/purrr/tests/testthat/test-deprec-map.R
/usr/lib64/R/library/purrr/tests/testthat/test-deprec-prepend.R
/usr/lib64/R/library/purrr/tests/testthat/test-deprec-rerun.R
/usr/lib64/R/library/purrr/tests/testthat/test-deprec-splice.R
/usr/lib64/R/library/purrr/tests/testthat/test-deprec-utils.R
/usr/lib64/R/library/purrr/tests/testthat/test-deprec-when.R
/usr/lib64/R/library/purrr/tests/testthat/test-detect.R
/usr/lib64/R/library/purrr/tests/testthat/test-every-some-none.R
/usr/lib64/R/library/purrr/tests/testthat/test-head-tail.R
/usr/lib64/R/library/purrr/tests/testthat/test-imap.R
/usr/lib64/R/library/purrr/tests/testthat/test-keep.R
/usr/lib64/R/library/purrr/tests/testthat/test-list-combine.R
/usr/lib64/R/library/purrr/tests/testthat/test-list-flatten.R
/usr/lib64/R/library/purrr/tests/testthat/test-list-modify.R
/usr/lib64/R/library/purrr/tests/testthat/test-list-simplify.R
/usr/lib64/R/library/purrr/tests/testthat/test-list-transpose.R
/usr/lib64/R/library/purrr/tests/testthat/test-lmap.R
/usr/lib64/R/library/purrr/tests/testthat/test-map-depth.R
/usr/lib64/R/library/purrr/tests/testthat/test-map-if-at.R
/usr/lib64/R/library/purrr/tests/testthat/test-map-mapper.R
/usr/lib64/R/library/purrr/tests/testthat/test-map-raw.R
/usr/lib64/R/library/purrr/tests/testthat/test-map.R
/usr/lib64/R/library/purrr/tests/testthat/test-map2.R
/usr/lib64/R/library/purrr/tests/testthat/test-modify-tree.R
/usr/lib64/R/library/purrr/tests/testthat/test-modify.R
/usr/lib64/R/library/purrr/tests/testthat/test-pluck-assign.R
/usr/lib64/R/library/purrr/tests/testthat/test-pluck-depth.R
/usr/lib64/R/library/purrr/tests/testthat/test-pluck.R
/usr/lib64/R/library/purrr/tests/testthat/test-pmap.R
/usr/lib64/R/library/purrr/tests/testthat/test-rate.R
/usr/lib64/R/library/purrr/tests/testthat/test-reduce.R
/usr/lib64/R/library/purrr/tests/testthat/test-superseded-flatten.R
/usr/lib64/R/library/purrr/tests/testthat/test-superseded-map-df.R
/usr/lib64/R/library/purrr/tests/testthat/test-superseded-simplify.R
/usr/lib64/R/library/purrr/tests/testthat/test-superseded-transpose.R
/usr/lib64/R/library/purrr/tests/testthat/test-utils.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/purrr/libs/purrr.so
/usr/lib64/R/library/purrr/libs/purrr.so.avx2
/usr/lib64/R/library/purrr/libs/purrr.so.avx512
