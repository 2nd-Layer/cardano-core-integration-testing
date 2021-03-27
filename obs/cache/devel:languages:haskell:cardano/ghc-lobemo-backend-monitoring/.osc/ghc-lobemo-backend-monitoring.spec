#
# spec file for package ghc-lobemo-backend-monitoring
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


%global pkg_name lobemo-backend-monitoring
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.1.0.0
Release:        0
Summary:        Provides a backend implementation for monitoring
License:        Apache-2.0
URL:            https://github.com/input-output-hk/iohk-monitoring-framework/
Source0:        %{pkg_name}-%{version}.tar.xz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-iohk-monitoring-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-safe-exceptions-devel
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-unordered-containers-devel
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-clock-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-contra-tracer-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-libyaml-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-semigroups-devel
BuildRequires:  ghc-split-devel
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-hunit-devel
BuildRequires:  ghc-tasty-quickcheck-devel
BuildRequires:  ghc-temporary-devel
BuildRequires:  ghc-time-units-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-void-devel
BuildRequires:  ghc-yaml-devel
%endif

%description
Provides a backend implementation for monitoring.

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
%license LICENSE
%license NOTICE

%files devel -f %{name}-devel.files
%doc README.md

%changelog
