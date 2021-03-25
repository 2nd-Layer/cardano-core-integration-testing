#
# spec file for package ghc-goblins
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


%global pkg_name goblins
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.2.0.0
Release:        0
Summary:        Genetic algorithm based randomised testing
License:        BSD-3-Clause
URL:            https://github.com/input-output-hk/goblins
Source0:        %{pkg_name}-%{version}.tar.xz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-bimap-devel
BuildRequires:  ghc-binary-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-extra-devel
BuildRequires:  ghc-hedgehog-devel
BuildRequires:  ghc-microlens-devel
BuildRequires:  ghc-microlens-mtl-devel
BuildRequires:  ghc-microlens-th-devel
BuildRequires:  ghc-mmorph-devel
BuildRequires:  ghc-monad-control-devel
BuildRequires:  ghc-moo-devel
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-th-utilities-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-tree-diff-devel
BuildRequires:  ghc-typerep-map-devel
%if %{with tests}
BuildRequires:  ghc-temporary-devel
%endif

%description
Genetic algorithm based randomised testing.

%package devel
Summary:        Haskell %{pkg_name} library development files
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description devel
This package provides the Haskell %{pkg_name} library development files.

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
%license LICENSE

%files devel -f %{name}-devel.files
%doc CHANGELOG.md

%changelog
