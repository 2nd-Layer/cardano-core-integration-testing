#
# spec file for package ghc-cardano-wallet-core-integration
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


%global pkg_name cardano-wallet-core-integration
Name:           ghc-%{pkg_name}
Version:        2020.11.03
Release:        0
Summary:        Core integration test library
License:        Apache-2.0
URL:            https://github.com/input-output-hk/cardano-wallet/tree/master/lib/core-integration
Source0:        %{pkg_name}-%{version}.tar.xz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-aeson-qq-devel
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-base58-bytestring-devel
BuildRequires:  ghc-bech32-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-cardano-addresses-devel
BuildRequires:  ghc-cardano-crypto-devel
BuildRequires:  ghc-cardano-transactions-devel
BuildRequires:  ghc-cardano-wallet-cli-devel
BuildRequires:  ghc-cardano-wallet-core-devel
BuildRequires:  ghc-cardano-wallet-launcher-devel
BuildRequires:  ghc-cardano-wallet-test-utils-devel
BuildRequires:  ghc-cborg-devel
BuildRequires:  ghc-command-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-criterion-measurement-devel
BuildRequires:  ghc-cryptonite-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-extra-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-fmt-devel
BuildRequires:  ghc-generic-lens-devel
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-hspec-expectations-lifted-devel
BuildRequires:  ghc-http-api-data-devel
BuildRequires:  ghc-http-client-devel
BuildRequires:  ghc-http-types-devel
BuildRequires:  ghc-iohk-monitoring-devel
BuildRequires:  ghc-lens-aeson-devel
BuildRequires:  ghc-memory-devel
BuildRequires:  ghc-optparse-applicative-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-resourcet-devel
BuildRequires:  ghc-retry-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-say-devel
BuildRequires:  ghc-scrypt-devel
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-temporary-devel
BuildRequires:  ghc-text-class-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel

%description
Shared core functionality for our integration test suites.

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

%post devel
%ghc_pkg_recache

%postun devel
%ghc_pkg_recache

%files -f %{name}.files

%files devel -f %{name}-devel.files

%changelog
