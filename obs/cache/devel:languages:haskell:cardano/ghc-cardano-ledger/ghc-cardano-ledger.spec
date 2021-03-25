#
# spec file for package ghc-cardano-ledger
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


%global pkg_name cardano-ledger
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.1.0.0
Release:        0
Summary:        The blockchain layer of Cardano
License:        Apache-2.0
URL:            https://github.com/input-output-hk/cardano-ledger-specs/tree/master/byron/ledger
Source0:        %{pkg_name}-%{version}.tar.xz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-base58-bytestring-devel
BuildRequires:  ghc-bimap-devel
BuildRequires:  ghc-binary-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-canonical-json-devel
BuildRequires:  ghc-cardano-binary-devel
BuildRequires:  ghc-cardano-crypto-devel
BuildRequires:  ghc-cardano-crypto-wrapper-devel
BuildRequires:  ghc-cardano-prelude-devel
BuildRequires:  ghc-cborg-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-contra-tracer-devel
BuildRequires:  ghc-cryptonite-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-digest-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-formatting-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-nothunks-devel
BuildRequires:  ghc-quiet-devel
BuildRequires:  ghc-resourcet-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-streaming-binary-devel
BuildRequires:  ghc-streaming-bytestring-devel
BuildRequires:  ghc-streaming-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-vector-devel
%if %{with tests}
BuildRequires:  ghc-base16-bytestring-devel
BuildRequires:  ghc-byron-spec-chain-devel
BuildRequires:  ghc-byron-spec-ledger-devel
BuildRequires:  ghc-cardano-binary-test-devel
BuildRequires:  ghc-cardano-crypto-test-devel
BuildRequires:  ghc-cardano-prelude-test-devel
BuildRequires:  ghc-generic-monoid-devel
BuildRequires:  ghc-hedgehog-devel
BuildRequires:  ghc-microlens-devel
BuildRequires:  ghc-optparse-applicative-devel
BuildRequires:  ghc-small-steps-devel
BuildRequires:  ghc-small-steps-test-devel
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-hedgehog-devel
%endif

%description
The blockchain layer of Cardano.

%package devel
Summary:        Haskell %{pkg_name} library development files
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description devel
This package provides the Haskell %{pkg_name} library development files.

%prep
%setup -q -n %{pkg_name}-%{version}
cabal-tweak-dep-ver streaming-binary '<0.3' '<0.4'

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
%doc README.md

%changelog
