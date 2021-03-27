#
# spec file for package cardano-wallet
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


%global pkg_name cardano-wallet
%bcond_with tests
Name:           %{pkg_name}
Version:        2020.11.26
Release:        0
Summary:        Wallet backend protocol-specific bits implemented using Shelley nodes
License:        Apache-2.0
URL:            https://github.com/input-output-hk/cardano-wallet/tree/master/lib/shelley
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  chrpath
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-Win32-network-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-base58-bytestring-devel
BuildRequires:  ghc-bech32-devel
BuildRequires:  ghc-bech32-th-devel
BuildRequires:  ghc-binary-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-cardano-addresses-devel
BuildRequires:  ghc-cardano-api-devel
BuildRequires:  ghc-cardano-binary-devel
BuildRequires:  ghc-cardano-crypto-class-devel
BuildRequires:  ghc-cardano-crypto-devel
BuildRequires:  ghc-cardano-crypto-wrapper-devel
BuildRequires:  ghc-cardano-ledger-devel
BuildRequires:  ghc-cardano-slotting-devel
BuildRequires:  ghc-cardano-wallet-cli-devel
BuildRequires:  ghc-cardano-wallet-core-devel
BuildRequires:  ghc-cardano-wallet-core-integration-devel
BuildRequires:  ghc-cardano-wallet-launcher-devel
BuildRequires:  ghc-cardano-wallet-test-utils-devel
BuildRequires:  ghc-cborg-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-contra-tracer-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-extra-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-fmt-devel
BuildRequires:  ghc-generic-lens-devel
BuildRequires:  ghc-io-sim-classes-devel
BuildRequires:  ghc-iohk-monitoring-devel
BuildRequires:  ghc-memory-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-network-mux-devel
BuildRequires:  ghc-optparse-applicative-devel
BuildRequires:  ghc-ouroboros-consensus-byron-devel
BuildRequires:  ghc-ouroboros-consensus-cardano-devel
BuildRequires:  ghc-ouroboros-consensus-devel
BuildRequires:  ghc-ouroboros-consensus-shelley-devel
BuildRequires:  ghc-ouroboros-network-devel
BuildRequires:  ghc-ouroboros-network-framework-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-retry-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-servant-server-devel
BuildRequires:  ghc-shelley-spec-ledger-devel
BuildRequires:  ghc-temporary-devel
BuildRequires:  ghc-text-class-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-warp-devel
BuildRequires:  ghc-yaml-devel
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-http-client-devel
BuildRequires:  ghc-stm-devel
%endif

%description
Wallet backend protocol-specific bits implemented using Shelley nodes.

%package -n ghc-%{name}
Summary:        Haskell %{name} library

%description -n ghc-%{name}
This package provides the Haskell %{name} shared library.

%package -n ghc-%{name}-devel
Summary:        Haskell %{name} library development files
Requires:       ghc-%{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description -n ghc-%{name}-devel
This package provides the Haskell %{name} library development files.

%prep
%setup -q

%build
%ghc_lib_build

%install
%ghc_lib_install
%ghc_fix_rpath %{pkg_name}-%{version}

%check
%cabal_test

%post -n ghc-%{name}-devel
%ghc_pkg_recache

%postun -n ghc-%{name}-devel
%ghc_pkg_recache

%files
%{_bindir}/%{name}
%{_bindir}/shelley-test-cluster

%files -n ghc-%{name} -f ghc-%{name}.files

%files -n ghc-%{name}-devel -f ghc-%{name}-devel.files

%changelog
