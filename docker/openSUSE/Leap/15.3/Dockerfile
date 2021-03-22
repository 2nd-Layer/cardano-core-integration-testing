FROM opensuse/leap:15.3

ENV CARDANO_NODE_VERSION="1.26.0"

RUN zypper refresh -s && \
  zypper -n dist-upgrade && \
  zypper -n install cabal-install \
    git-core \
    ghc

WORKDIR /usr/src
RUN git clone --recurse-submodules https://github.com/input-output-hk/cardano-node
WORKDIR /usr/src/cardano-node
RUN git fetch --all
RUN git checkout ${CARDANO_NODE_VERSION}
RUN scripts/gen-cabal-nosystemd.sh
COPY cabal.project.local ./

RUN cabal new-build \
  --allow-newer \
  --dry-run \
  --only-configure \
  --project-file=cabal.nosystemd.project \
  all
