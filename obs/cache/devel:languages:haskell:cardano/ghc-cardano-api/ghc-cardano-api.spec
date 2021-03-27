#
# spec file for package ghc-cardano-api
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


%global pkg_name cardano-api
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        1.22.1
Release:        0
Summary:        FIXME
License:        Apache-2.0
URL:            https://github.com/input-output-hk/cardano-node/tree/master/cardano-api
Source0:        %{pkg_name}-%{version}.tar.xz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-aeson-pretty-devel
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-base16-bytestring-devel
BuildRequires:  ghc-base58-bytestring-devel
BuildRequires:  ghc-base64-devel
BuildRequires:  ghc-bech32-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-cardano-binary-devel
BuildRequires:  ghc-cardano-config-devel
BuildRequires:  ghc-cardano-crypto-class-devel
BuildRequires:  ghc-cardano-crypto-devel
BuildRequires:  ghc-cardano-crypto-wrapper-devel
BuildRequires:  ghc-cardano-ledger-devel
BuildRequires:  ghc-cardano-prelude-devel
BuildRequires:  ghc-cardano-slotting-devel
BuildRequires:  ghc-cborg-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-contra-tracer-devel
BuildRequires:  ghc-cryptonite-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-formatting-devel
BuildRequires:  ghc-io-sim-classes-devel
BuildRequires:  ghc-iohk-monitoring-devel
BuildRequires:  ghc-iproute-devel
BuildRequires:  ghc-memory-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-network-mux-devel
BuildRequires:  ghc-network-uri-devel
BuildRequires:  ghc-nothunks-devel
BuildRequires:  ghc-ouroboros-consensus-byron-devel
BuildRequires:  ghc-ouroboros-consensus-cardano-devel
BuildRequires:  ghc-ouroboros-consensus-devel
BuildRequires:  ghc-ouroboros-consensus-shelley-devel
BuildRequires:  ghc-ouroboros-network-devel
BuildRequires:  ghc-ouroboros-network-framework-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-scientific-devel
BuildRequires:  ghc-serialise-devel
BuildRequires:  ghc-shelley-spec-ledger-devel
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-except-devel
BuildRequires:  ghc-typed-protocols-devel
BuildRequires:  ghc-typed-protocols-examples-devel
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-vector-devel
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-cardano-crypto-test-devel
BuildRequires:  ghc-cardano-crypto-tests-devel
BuildRequires:  ghc-cardano-ledger-test-devel
BuildRequires:  ghc-cardano-prelude-test-devel
BuildRequires:  ghc-hedgehog-devel
BuildRequires:  ghc-shelley-spec-ledger-test-devel
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-hedgehog-devel
BuildRequires:  ghc-tasty-quickcheck-devel
%endif

%description
The cardano api.

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
%license LICENSE
%license NOTICE

%files devel -f %{name}-devel.files
%doc ChangeLog.md README.md

%changelog
