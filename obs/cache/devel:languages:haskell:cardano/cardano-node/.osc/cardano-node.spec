#
# spec file for package cardano-node
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


%global pkg_name cardano-node
%bcond_with tests
Name:           %{pkg_name}
Version:        1.22.1
Release:        0
Summary:        The Cardano full node in Haskell
License:        Apache-2.0
URL:            https://github.com/input-output-hk/cardano-node
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  chrpath
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-base16-bytestring-devel
BuildRequires:  ghc-byron-spec-ledger-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-cardano-api-devel
BuildRequires:  ghc-cardano-config-devel
BuildRequires:  ghc-cardano-crypto-class-devel
BuildRequires:  ghc-cardano-crypto-wrapper-devel
BuildRequires:  ghc-cardano-ledger-devel
BuildRequires:  ghc-cardano-prelude-devel
BuildRequires:  ghc-cardano-slotting-devel
BuildRequires:  ghc-cborg-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-contra-tracer-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-dns-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-generic-data-devel
BuildRequires:  ghc-hedgehog-extras-devel
BuildRequires:  ghc-hostname-devel
BuildRequires:  ghc-io-sim-classes-devel
BuildRequires:  ghc-iohk-monitoring-devel
BuildRequires:  ghc-iproute-devel
BuildRequires:  ghc-lobemo-backend-aggregation-devel
BuildRequires:  ghc-lobemo-backend-ekg-devel
BuildRequires:  ghc-lobemo-backend-monitoring-devel
BuildRequires:  ghc-lobemo-backend-trace-forwarder-devel
BuildRequires:  ghc-lobemo-scribe-systemd-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-network-mux-devel
BuildRequires:  ghc-nothunks-devel
BuildRequires:  ghc-optparse-applicative-devel
BuildRequires:  ghc-ouroboros-consensus-byron-devel
BuildRequires:  ghc-ouroboros-consensus-cardano-devel
BuildRequires:  ghc-ouroboros-consensus-devel
BuildRequires:  ghc-ouroboros-consensus-shelley-devel
BuildRequires:  ghc-ouroboros-network-devel
BuildRequires:  ghc-ouroboros-network-framework-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-safe-exceptions-devel
BuildRequires:  ghc-scientific-devel
BuildRequires:  ghc-shelley-spec-ledger-devel
BuildRequires:  ghc-strict-concurrency-devel
BuildRequires:  ghc-systemd-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-tracer-transformers-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-except-devel
BuildRequires:  ghc-typed-protocols-devel
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-yaml-devel
%if %{with tests}
BuildRequires:  ghc-cardano-crypto-test-devel
BuildRequires:  ghc-cardano-prelude-test-devel
BuildRequires:  ghc-cryptonite-devel
BuildRequires:  ghc-hedgehog-corpus-devel
BuildRequires:  ghc-hedgehog-devel
BuildRequires:  ghc-mmorph-devel
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-resourcet-devel
BuildRequires:  ghc-shelley-spec-ledger-test-devel
BuildRequires:  ghc-temporary-devel
BuildRequires:  ghc-unliftio-devel
%endif

%description
The core component that is used to participate in a Cardano decentralised blockchain.

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
%license LICENSE
%license NOTICE
%doc ChangeLog.md
%{_bindir}/%{name}

%files -n ghc-%{name} -f ghc-%{name}.files
%license LICENSE
%license NOTICE

%files -n ghc-%{name}-devel -f ghc-%{name}-devel.files
%doc ChangeLog.md

%changelog
