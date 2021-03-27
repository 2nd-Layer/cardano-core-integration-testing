#
# spec file for package ghc-text-class
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


%global pkg_name text-class
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        2020.12.8
Release:        0
Summary:        Extra helpers to convert data-types to and from Text
License:        Apache-2.0
URL:            https://github.com/input-output-hk/cardano-wallet/tree/master/lib/text-class
Source0:        %{pkg_name}-%{version}.tar.xz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-OddWord-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-casing-devel
BuildRequires:  ghc-extra-devel
BuildRequires:  ghc-fmt-devel
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel

%description
Extra helpers to convert data-types to and from Text.

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
cabal-tweak-flag release True

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

%files devel -f %{name}-devel.files

%changelog
