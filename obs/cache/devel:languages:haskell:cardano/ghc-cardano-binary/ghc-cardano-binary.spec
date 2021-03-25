#
# spec file for package ghc-cardano-binary
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


%global pkg_name cardano-binary
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        1.5.0
Release:        0
Summary:        Binary serialization for Cardano
License:        Apache-2.0
URL:            https://github.com/input-output-hk/cardano-base/binary
Source0:        %{version}/%{pkg_name}-%{version}.tar.xz
Patch0:         67246568db5ef45ffd2e25af08e2cb2e00ec220c.patch
Patch1:         fix-cabal-recursion-schemes-dependency.patch
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-cardano-prelude-devel
BuildRequires:  ghc-cborg-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-digest-devel
BuildRequires:  ghc-formatting-devel
BuildRequires:  ghc-nothunks-devel
BuildRequires:  ghc-primitive-devel
BuildRequires:  ghc-recursion-schemes-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-safe-exceptions-devel
BuildRequires:  ghc-tagged-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-vector-devel
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-cardano-prelude-test-devel
BuildRequires:  ghc-hedgehog-devel
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-pretty-show-devel
BuildRequires:  ghc-quickcheck-instances-devel
%endif

%description
This package includes the binary serialization format for Cardano.

%package devel
Summary:        Haskell %{pkg_name} library development files
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description devel
This package provides the Haskell %{pkg_name} library development files.

%prep
%autosetup -n %{pkg_name}-%{version} -p2

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
%doc README.md

%changelog
