FROM opensuse/leap:15.3

ENV CARDANO_NODE_VERSION="1.26.0"

RUN zypper -n \
  addrepo \
  https://download.opensuse.org/repositories/devel:/languages:/haskell/openSUSE_Leap_15.3/devel:languages:haskell.repo

RUN zypper --gpg-auto-import-keys refresh -s
RUN zypper -n dist-upgrade
RUN zypper -n install cabal-install \
      git-core \
      ghc-devel \
      jq \
      libsodium-devel

WORKDIR /usr/src
RUN git clone --recurse-submodules https://github.com/input-output-hk/cardano-node
WORKDIR /usr/src/cardano-node
RUN git fetch --all
RUN git checkout ${CARDANO_NODE_VERSION}
RUN scripts/gen-cabal-nosystemd.sh
COPY cabal.project.local ./

RUN cabal new-update
RUN cabal new-build \
  --allow-newer \
  --allow-older \
  --dry-run \
  --only-configure \
  --project-file=cabal.nosystemd.project \
  -f -external-libsodium-vrf \
  all

WORKDIR /usr/src
COPY plan2rpms.sh ./
RUN ./plan2rpms.sh
RUN cat installable-hackage-dependencies.txt | xargs zypper -n install

WORKDIR /usr/src/cardano-node
RUN cabal new-build \
  --allow-newer \
  --allow-older \
  --project-file=cabal.nosystemd.project \
  -f -external-libsodium-vrf \
  all
