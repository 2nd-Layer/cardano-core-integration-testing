FROM opensuse/leap:15.3 AS planner

ARG APPLICATION="cardano-node"
ARG APPLICATION_VERSION="master"

RUN zypper -n \
  addrepo \
  https://download.opensuse.org/repositories/devel:/languages:/haskell/openSUSE_Leap_15.3/devel:languages:haskell.repo

RUN zypper --gpg-auto-import-keys refresh devel_languages_haskell
RUN zypper refresh -s
RUN zypper -n dist-upgrade
RUN zypper -n install cabal-install \
      git-core \
      ghc-devel \
      jq \
      libsodium-devel

COPY plan2rpms.sh /usr/local/bin/

WORKDIR /usr/src
RUN git clone --recurse-submodules https://github.com/input-output-hk/${APPLICATION}
WORKDIR /usr/src/${APPLICATION}
RUN git fetch --all
RUN git checkout ${APPLICATION_VERSION}
RUN scripts/gen-cabal-nosystemd.sh
COPY cabal.project.local ./

RUN cabal new-update
RUN cabal new-build \
  --allow-newer \
  --allow-older \
  --avoid-reinstalls \
  --dry-run \
  --only-configure \
  --project-file=cabal.nosystemd.project \
  -f -external-libsodium-vrf \
  all

WORKDIR /usr/src
RUN plan2rpms.sh
RUN cat installable-hackage-dependencies.txt | xargs zypper -n install

WORKDIR /usr/src/${APPLICATION}
RUN cabal new-build \
  --allow-newer \
  --allow-older \
  --avoid-reinstalls \
  --dry-run \
  --only-configure \
  --project-file=cabal.nosystemd.project \
  -f -external-libsodium-vrf \
  all

WORKDIR /usr/src
RUN rm *.txt
RUN ./plan2rpms.sh

FROM scratch AS exporter
COPY --from=planner \
  /usr/src/${APPLICATION}/plan*.json \
  ./

FROM planner AS builder

WORKDIR /usr/src/${APPLICATION}
RUN cabal new-build \
  --allow-newer \
  --allow-older \
  --avoid-reinstalls \
  --project-file=cabal.nosystemd.project \
  -f -external-libsodium-vrf \
  all