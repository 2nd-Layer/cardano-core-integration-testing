#
# spec file for package ghc-cardano-wallet-launcher
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


%global pkg_name cardano-wallet-launcher
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        2020.11.03
Release:        0
Summary:        Utilities for a building commands launcher
License:        Apache-2.0
URL:            https://github.com/input-output-hk/cardano-wallet/tree/master/lib/launcher
Source0:        %{pkg_name}-%{version}.tar.xz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-code-page-devel
BuildRequires:  ghc-contra-tracer-devel
BuildRequires:  ghc-extra-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-fmt-devel
BuildRequires:  ghc-iohk-monitoring-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-text-class-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-unix-devel
%if %{with tests}
BuildRequires:  ghc-cardano-wallet-test-utils-devel
BuildRequires:  ghc-hspec-core-devel
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-hspec-expectations-devel
BuildRequires:  ghc-retry-devel
BuildRequires:  ghc-time-devel
%endif

%description
Utilities for a building commands launcher.

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

%check
%cabal_test

%post devel
%ghc_pkg_recache

%postun devel
%ghc_pkg_recache

%files -f %{name}.files

%files devel -f %{name}-devel.files

%changelog
