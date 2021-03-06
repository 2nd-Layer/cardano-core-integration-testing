#
# spec file for package ghc-ouroboros-consensus-cardano
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


%global pkg_name ouroboros-consensus-cardano
Name:           ghc-%{pkg_name}
Version:        0.1.0.0
Release:        0
Summary:        The instantation of the Ouroboros consensus layer used by Cardano
License:        Apache-2.0
URL:            https://github.com/input-output-hk/ouroboros-network/tree/master/ouroboros-consensus-cardano
Source0:        %{pkg_name}-%{version}.tar.xz
BuildRequires:  chrpath
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-cardano-binary-devel
BuildRequires:  ghc-cardano-crypto-class-devel
BuildRequires:  ghc-cardano-crypto-wrapper-devel
BuildRequires:  ghc-cardano-ledger-devel
BuildRequires:  ghc-cardano-ledger-shelley-ma-devel
BuildRequires:  ghc-cardano-prelude-devel
BuildRequires:  ghc-cardano-slotting-devel
BuildRequires:  ghc-cborg-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-contra-tracer-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-nothunks-devel
BuildRequires:  ghc-optparse-applicative-devel
BuildRequires:  ghc-ouroboros-consensus-byron-devel
BuildRequires:  ghc-ouroboros-consensus-devel
BuildRequires:  ghc-ouroboros-consensus-shelley-devel
BuildRequires:  ghc-ouroboros-network-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-serialise-devel
BuildRequires:  ghc-shelley-spec-ledger-devel
BuildRequires:  ghc-text-devel

%description
The instantation of the Ouroboros consensus layer used by Cardano.

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

%post devel
%ghc_pkg_recache

%postun devel
%ghc_pkg_recache

%files -f %{name}.files
%license LICENSE
%license NOTICE
%{_bindir}/db-analyser

%files devel -f %{name}-devel.files

%changelog
