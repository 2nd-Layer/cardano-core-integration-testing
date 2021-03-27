#
# spec file for package ghc-io-sim-classes
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


%global pkg_name io-sim-classes
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.2.0.0
Release:        0
Summary:        Type classes for concurrency with STM, ST and timing
License:        Apache-2.0
URL:            https://github.com/input-output-hk/ouroboros-network/tree/master/io-sim-classes
Source0:        %{pkg_name}-%{version}.tar.xz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-time-devel
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-quickcheck-devel
%endif

%description
Type classes for concurrency with STM, ST and timing.

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
cabal-tweak-dep-ver base '<4.15' '<5'

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
%license NOTICE

%files devel -f %{name}-devel.files

%changelog
