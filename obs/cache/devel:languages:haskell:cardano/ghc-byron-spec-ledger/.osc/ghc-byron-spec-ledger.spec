#
# spec file for package ghc-byron-spec-ledger
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


%global pkg_name byron-spec-ledger
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.1.0.0
Release:        0
Summary:        Executable specification of Cardano ledger
License:        MIT
URL:            https://github.com/input-output-hk/cardano-ledger-specs/tree/master/byron
Source0:        %{pkg_name}-%{version}.tar.xz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-Unique-devel
BuildRequires:  ghc-bimap-devel
BuildRequires:  ghc-cardano-binary-devel
BuildRequires:  ghc-cardano-prelude-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-file-embed-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-goblins-devel
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-hedgehog-devel
BuildRequires:  ghc-microlens-devel
BuildRequires:  ghc-microlens-th-devel
BuildRequires:  ghc-nothunks-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-small-steps-devel
BuildRequires:  ghc-small-steps-test-devel
BuildRequires:  ghc-template-haskell-devel
%if %{with tests}
BuildRequires:  ghc-doctest-devel
BuildRequires:  ghc-memory-devel
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-hedgehog-devel
BuildRequires:  ghc-tasty-hunit-devel
BuildRequires:  ghc-text-devel
%endif

%description
Executable specification of Cardano ledger.

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

%check
%cabal_test

%post devel
%ghc_pkg_recache

%postun devel
%ghc_pkg_recache

%files -f %{name}.files

%files devel -f %{name}-devel.files
%doc CHANGELOG.md

%changelog
