#
# spec file for package ghc-cardano-config
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


%global pkg_name cardano-config
Name:           ghc-%{pkg_name}
Version:        0.1.0.0
Release:        0
Summary:        Types and functions necessary to configure cardano-node
License:        Apache-2.0
URL:            https://github.com/input-output-hk
Source0:        %{pkg_name}-%{version}.tar.xz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-cardano-prelude-devel
BuildRequires:  ghc-file-embed-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-text-devel

%description
This package exposes the types and functions necessary to configure the cardano-node.

%package devel
Summary:        Haskell %{pkg_name} library development files
Requires:       ghc-%{pkg_name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description devel
This package provides the Haskell %{pkg_name} library development files.

%prep
%autosetup -n cardano-config-%{version}

%build
%define cabal_configure_options -f-systemd
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
%doc README.md

%files devel -f %{name}-devel.files
%doc README.md

%changelog
