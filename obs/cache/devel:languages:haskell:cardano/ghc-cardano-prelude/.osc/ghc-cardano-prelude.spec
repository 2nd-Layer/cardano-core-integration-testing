#
# spec file for package ghc-cardano-prelude
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


%global pkg_name cardano-prelude
Name:           ghc-%{pkg_name}
Version:        0.1.0.0
Release:        0
Summary:        A Prelude replacement for the Cardano project
License:        MIT
URL:            https://github.com/input-output-hk/cardano-prelude
Source0:        cardano-prelude-%{version}.tar.xz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-base16-bytestring-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-canonical-json-devel
BuildRequires:  ghc-cborg-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-fingertree-devel
BuildRequires:  ghc-formatting-devel
BuildRequires:  ghc-ghc-heap-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-nothunks-devel
BuildRequires:  ghc-protolude-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-serialise-devel
BuildRequires:  ghc-tagged-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-vector-devel

%description
A Prelude replacement for the Cardano project.

%package devel
Summary:        Haskell %{pkg_name} library development files
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description devel
This package provides the Haskell %{pkg_name} library development files.

%prep
%autosetup -n cardano-prelude-%{version}

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
%doc ChangeLog.md README.md

%files devel -f %{name}-devel.files
%doc ChangeLog.md README.md

%changelog
