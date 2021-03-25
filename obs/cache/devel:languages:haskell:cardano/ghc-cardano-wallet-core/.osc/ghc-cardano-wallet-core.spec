#
# spec file for package ghc-cardano-wallet-core
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


%global pkg_name cardano-wallet-core
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        2020.11.26
Release:        0
Summary:        The Wallet Backend for a Cardano node
License:        Apache-2.0
URL:            https://github.com/input-output-hk/cardano-wallet/tree/master/lib/core
Source0:        %{pkg_name}-%{version}.tar.xz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-OddWord-devel
BuildRequires:  ghc-Win32-network-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-bech32-devel
BuildRequires:  ghc-bech32-th-devel
BuildRequires:  ghc-binary-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-cardano-addresses-devel
BuildRequires:  ghc-cardano-api-devel
BuildRequires:  ghc-cardano-crypto-devel
BuildRequires:  ghc-cardano-slotting-devel
BuildRequires:  ghc-cborg-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-contra-tracer-devel
BuildRequires:  ghc-cryptonite-devel
BuildRequires:  ghc-data-default-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-digest-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-either-devel
BuildRequires:  ghc-errors-devel
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-extra-devel
BuildRequires:  ghc-fast-logger-devel
BuildRequires:  ghc-file-embed-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-fmt-devel
BuildRequires:  ghc-foldl-devel
BuildRequires:  ghc-generic-lens-devel
BuildRequires:  ghc-http-api-data-devel
BuildRequires:  ghc-http-client-devel
BuildRequires:  ghc-http-client-tls-devel
BuildRequires:  ghc-http-media-devel
BuildRequires:  ghc-http-types-devel
BuildRequires:  ghc-io-sim-classes-devel
BuildRequires:  ghc-iohk-monitoring-devel
BuildRequires:  ghc-memory-devel
BuildRequires:  ghc-monad-logger-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-network-uri-devel
BuildRequires:  ghc-ntp-client-devel
BuildRequires:  ghc-ouroboros-consensus-devel
BuildRequires:  ghc-ouroboros-network-devel
BuildRequires:  ghc-path-pieces-devel
BuildRequires:  ghc-persistent-devel
BuildRequires:  ghc-persistent-sqlite-devel
BuildRequires:  ghc-persistent-template-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-random-shuffle-devel
BuildRequires:  ghc-retry-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-safe-devel
BuildRequires:  ghc-safe-exceptions-devel
BuildRequires:  ghc-scientific-devel
BuildRequires:  ghc-scrypt-devel
BuildRequires:  ghc-servant-client-devel
BuildRequires:  ghc-servant-devel
BuildRequires:  ghc-servant-server-devel
BuildRequires:  ghc-split-devel
BuildRequires:  ghc-statistics-devel
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-streaming-commons-devel
BuildRequires:  ghc-string-qq-devel
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-text-class-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-tls-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-typed-protocols-devel
BuildRequires:  ghc-unliftio-devel
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-wai-devel
BuildRequires:  ghc-warp-devel
BuildRequires:  ghc-warp-tls-devel
BuildRequires:  ghc-x509-devel
BuildRequires:  ghc-x509-store-devel
BuildRequires:  ghc-x509-validation-devel
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-aeson-qq-devel
BuildRequires:  ghc-cardano-wallet-launcher-devel
BuildRequires:  ghc-cardano-wallet-test-utils-devel
BuildRequires:  ghc-connection-devel
BuildRequires:  ghc-generic-arbitrary-devel
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-lens-devel
BuildRequires:  ghc-quickcheck-state-machine-devel
BuildRequires:  ghc-servant-swagger-devel
BuildRequires:  ghc-swagger2-devel
BuildRequires:  ghc-temporary-devel
BuildRequires:  ghc-tree-diff-devel
BuildRequires:  ghc-wai-extra-devel
BuildRequires:  ghc-yaml-devel
%endif

%description
The Wallet Backend for a Cardano node.

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
