#
# spec file for package ghc-ouroboros-network
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


%global pkg_name ouroboros-network
%global has_internal_sub_libraries 1
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.1.0.0
Release:        0
Summary:        A networking layer for the Ouroboros blockchain protocol
License:        Apache-2.0
URL:            https://github.com/input-output-hk/ouroboros-network/tree/master/ouroboros-network
Source0:        %{pkg_name}-%{version}.tar.xz
Patch0:         fix-splitmix.patch
BuildRequires:  chrpath
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-base16-bytestring-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-cardano-binary-devel
BuildRequires:  ghc-cardano-prelude-devel
BuildRequires:  ghc-cardano-slotting-devel
BuildRequires:  ghc-cborg-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-contra-tracer-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-dns-devel
BuildRequires:  ghc-fingertree-devel
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-io-sim-classes-devel
BuildRequires:  ghc-io-sim-devel
BuildRequires:  ghc-iproute-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-network-mux-devel
BuildRequires:  ghc-nothunks-devel
BuildRequires:  ghc-ouroboros-network-framework-devel
BuildRequires:  ghc-pipes-devel
BuildRequires:  ghc-psqueues-devel
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-serialise-devel
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-quickcheck-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-typed-protocols-devel
%if %{with tests}
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-binary-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-ouroboros-network-testing-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-process-extras-devel
BuildRequires:  ghc-splitmix-devel
BuildRequires:  ghc-tasty-hunit-devel
%endif

%description
A networking layer for the Ouroboros blockchain protocol.

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
%patch0 -p1


%build
%ghc_lib_build_without_haddock

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
%license LICENSE
%license NOTICE
%{_bindir}/demo-chain-sync

%files devel -f %{name}-devel.files
%doc ChangeLog.md

%changelog
