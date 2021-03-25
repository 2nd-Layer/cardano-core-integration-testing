#
# spec file for package ghc-cardano-wallet-jormungandr
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


%global pkg_name cardano-wallet-jormungandr
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        2020.11.03
Release:        0
Summary:        Wallet backend protocol-specific bits implemented using Jörmungandr
License:        Apache-2.0
URL:            https://github.com/input-output-hk/cardano-wallet/tree/master/lib/jormungandr
Source0:        %{pkg_name}-%{version}.tar.xz
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
BuildRequires:  ghc-cardano-crypto-devel
BuildRequires:  ghc-cardano-wallet-cli-devel
BuildRequires:  ghc-cardano-wallet-core-devel
BuildRequires:  ghc-cardano-wallet-launcher-devel
BuildRequires:  ghc-conduit-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-contra-tracer-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-either-devel
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-extra-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-fmt-devel
BuildRequires:  ghc-generic-lens-devel
BuildRequires:  ghc-http-client-devel
BuildRequires:  ghc-http-conduit-devel
BuildRequires:  ghc-http-types-devel
BuildRequires:  ghc-iohk-monitoring-devel
BuildRequires:  ghc-lens-aeson-devel
BuildRequires:  ghc-lens-devel
BuildRequires:  ghc-lifted-base-devel
BuildRequires:  ghc-memory-devel
BuildRequires:  ghc-monad-control-devel
BuildRequires:  ghc-monad-loops-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-optparse-applicative-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-retry-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-safe-devel
BuildRequires:  ghc-servant-client-core-devel
BuildRequires:  ghc-servant-client-devel
BuildRequires:  ghc-servant-devel
BuildRequires:  ghc-servant-server-devel
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-temporary-devel
BuildRequires:  ghc-text-class-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-warp-devel
BuildRequires:  ghc-wreq-devel
BuildRequires:  ghc-zip-devel
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-aeson-qq-devel
BuildRequires:  ghc-cardano-wallet-core-integration-devel
BuildRequires:  ghc-cardano-wallet-test-utils-devel
BuildRequires:  ghc-cborg-devel
BuildRequires:  ghc-command-devel
BuildRequires:  ghc-file-embed-devel
BuildRequires:  ghc-generic-arbitrary-devel
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-hspec-expectations-lifted-devel
BuildRequires:  ghc-hspec-golden-aeson-devel
BuildRequires:  ghc-http-api-data-devel
BuildRequires:  ghc-servant-swagger-devel
BuildRequires:  ghc-swagger2-devel
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-yaml-devel
%endif

%description
Wallet backend protocol-specific bits implemented using Jörmungandr.

%package devel
Summary:        Haskell %{pkg_name} library development files
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description devel
This package provides the Haskell %{pkg_name} library
development files.

%prep
%setup -q -n %{pkg_name}-%{version}

%build
%ghc_lib_build

%install
%ghc_lib_install
%ghc_fix_rpath %{pkg_name}-%{version}

%check
%cabal_test

%post devel
%ghc_pkg_recache

%postun devel
%ghc_pkg_recache

%files -f %{name}.files
%{_bindir}/%{pkg_name}
%{_bindir}/migration-test

%files devel -f %{name}-devel.files
%doc README.md

%changelog
