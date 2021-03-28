FROM opensuse/leap:15.3

RUN zypper -n \
  addrepo \
  https://download.opensuse.org/repositories/devel:/languages:/haskell/openSUSE_Leap_15.3/devel:languages:haskell.repo

RUN zypper --gpg-auto-import-keys refresh devel_languages_haskell
RUN zypper refresh -s
RUN zypper -n dist-upgrade
RUN zypper -n install cabal-install \
      cabal2spec \
      git-core \
      ghc-devel \
      jq

COPY plan2rpms.sh /usr/local/bin/