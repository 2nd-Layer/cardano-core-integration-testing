#
# spec file for package ghc-small-steps-test
#
# Copyright (c) 2020 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%global pkg_name small-steps-test
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.1.0.0
Release:        0
Summary:        Small step semantics testing library
License:        Apache-2.0
URL:            https://github.com/input-output-hk/cardano-ledger-specs/tree/master/semantics/small-steps-test
Source0:        %{pkg_name}-%{version}.tar.xz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-cardano-crypto-class-devel
BuildRequires:  ghc-cardano-prelude-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-cryptonite-devel
BuildRequires:  ghc-free-devel
BuildRequires:  ghc-goblins-devel
BuildRequires:  ghc-hedgehog-devel
BuildRequires:  ghc-microlens-devel
BuildRequires:  ghc-microlens-th-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-nothunks-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-small-steps-devel
BuildRequires:  ghc-tasty-hunit-devel
BuildRequires:  ghc-transformers-devel
%if %{with tests}
BuildRequires:  ghc-Unique-devel
BuildRequires:  ghc-cardano-binary-devel
BuildRequires:  ghc-data-default-devel
BuildRequires:  ghc-doctest-devel
BuildRequires:  ghc-sequence-devel
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-expected-failure-devel
BuildRequires:  ghc-tasty-hedgehog-devel
BuildRequires:  ghc-tasty-quickcheck-devel
%endif

%description
Small step semantics testing library.

%package devel
Summary:        Haskell %{pkg_name} library development files
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description devel
This package provides the Haskell %{pkg_name} library development
files.

%prep
%setup -q -n %{pkg_name}-%{version}

%build
%ghc_lib_build

%install
%ghc_lib_install

%check
%cabal_test

%post devel
%ghc_pkg_recache

%postun devel
%ghc_pkg_recache

%files -f %{name}.files

%files devel -f %{name}-devel.files

%changelog
