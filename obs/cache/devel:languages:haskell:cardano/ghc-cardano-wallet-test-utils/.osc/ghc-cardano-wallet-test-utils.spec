#
# spec file for package ghc-cardano-wallet-test-utils
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


%global pkg_name cardano-wallet-test-utils
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        2020.12.8
Release:        0
Summary:        Shared utilities for writing unit and property tests
License:        Apache-2.0
URL:            https://github.com/input-output-hk/cardano-wallet/tree/master/lib/test-utils
Source0:        %{pkg_name}-%{version}.tar.xz
Patch0:         lens.patch
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-contra-tracer-devel
BuildRequires:  ghc-file-embed-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-lens-devel
BuildRequires:  ghc-hspec-core-devel
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-hspec-expectations-devel
BuildRequires:  ghc-hspec-golden-aeson-devel
BuildRequires:  ghc-http-api-data-devel
BuildRequires:  ghc-iohk-monitoring-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-wai-app-static-devel
BuildRequires:  ghc-warp-devel
%if %{with tests}
BuildRequires:  ghc-silently-devel
%endif

%description
Shared utilities for writing unit and property tests.

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
%autosetup -p1 -n %{pkg_name}-%{version}

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
