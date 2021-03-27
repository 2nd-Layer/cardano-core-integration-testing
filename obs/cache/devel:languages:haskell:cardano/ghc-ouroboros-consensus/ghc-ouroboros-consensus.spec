#
# spec file for package ghc-ouroboros-consensus
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%global pkg_name ouroboros-consensus
Name:           ghc-%{pkg_name}
Version:        0.1.0.0
Release:        0
Summary:        Consensus layer for the Ouroboros blockchain protocol
License:        Apache-2.0
URL:            https://github.com/input-output-hk/ouroboros-network/tree/master/ouroboros-consensus
Source0:        %{pkg_name}-%{version}.tar.xz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base16-bytestring-devel
BuildRequires:  ghc-bimap-devel
BuildRequires:  ghc-binary-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-cardano-binary-devel
BuildRequires:  ghc-cardano-crypto-class-devel
BuildRequires:  ghc-cardano-prelude-devel
BuildRequires:  ghc-cardano-slotting-devel
BuildRequires:  ghc-cborg-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-contra-tracer-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-digest-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-filelock-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-io-sim-classes-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-network-mux-devel
BuildRequires:  ghc-nothunks-devel
BuildRequires:  ghc-ouroboros-network-devel
BuildRequires:  ghc-ouroboros-network-framework-devel
BuildRequires:  ghc-psqueues-devel
BuildRequires:  ghc-quiet-devel
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-semialign-devel
BuildRequires:  ghc-serialise-devel
BuildRequires:  ghc-sop-core-devel
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-streaming-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-these-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-typed-protocols-devel
BuildRequires:  ghc-unix-bytestring-devel
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-vector-devel

%description
Consensus layer for the Ouroboros blockchain protocol.

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

%post devel
%ghc_pkg_recache

%postun devel
%ghc_pkg_recache

%files -f %{name}.files
%license LICENSE
%license NOTICE

%files devel -f %{name}-devel.files

%changelog
