#
# spec file for package ghc-ouroboros-consensus-byron
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


%global pkg_name ouroboros-consensus-byron
Name:           ghc-%{pkg_name}
Version:        0.1.0.0
Release:        0
Summary:        Byron ledger integration in the Ouroboros consensus layer
License:        Apache-2.0
URL:            https://github.com/input-output-hk/ouroboros-network/tree/master/ouroboros-consensus-byron
Source0:        %{pkg_name}-%{version}.tar.xz
Patch0:         disable-executable.patch
BuildRequires:  chrpath
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-cardano-binary-devel
BuildRequires:  ghc-cardano-crypto-class-devel
BuildRequires:  ghc-cardano-crypto-devel
BuildRequires:  ghc-cardano-crypto-wrapper-devel
BuildRequires:  ghc-cardano-ledger-devel
BuildRequires:  ghc-cardano-prelude-devel
BuildRequires:  ghc-cardano-slotting-devel
BuildRequires:  ghc-cborg-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-cryptonite-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-formatting-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-nothunks-devel
BuildRequires:  ghc-optparse-applicative-devel
BuildRequires:  ghc-optparse-generic-devel
BuildRequires:  ghc-ouroboros-consensus-devel
BuildRequires:  ghc-ouroboros-network-devel
BuildRequires:  ghc-path-devel
BuildRequires:  ghc-path-io-devel
BuildRequires:  ghc-resourcet-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-serialise-devel
BuildRequires:  ghc-streaming-devel
BuildRequires:  ghc-text-devel

%description
Byron ledger integration in the Ouroboros consensus layer.

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
%patch0 -p1
cabal-tweak-dep-ver formatting '<6.4' '<8'
cabal-tweak-dep-ver path '< 0.7' '< 1'

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

%files devel -f %{name}-devel.files

%changelog
