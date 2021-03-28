FROM osleap-plan2rpms as solver

ARG APPLICATION="cardano-wallet"
ARG APPLICATION_VERSION="master"

RUN zypper refresh -s
RUN zypper -n dist-upgrade
RUN zypper -n install libsodium-devel

WORKDIR /usr/src
RUN git clone --recurse-submodules https://github.com/input-output-hk/${APPLICATION}
WORKDIR /usr/src/${APPLICATION}
RUN git fetch --all
RUN git checkout ${APPLICATION_VERSION}
COPY cabal.project.local ./

RUN cabal new-update
RUN cabal new-build \
  --allow-newer \
  --allow-older \
  --disable-tests \
  --disable-benchmarks \
  --avoid-reinstalls \
  --dry-run \
  --only-configure \
  -f -external-libsodium-vrf \
  all

WORKDIR /usr/src
RUN plan2rpms.sh
RUN cat installable-hackage-dependencies.txt | grep -v ghc-loop | xargs zypper -n install

WORKDIR /usr/src/${APPLICATION}
RUN cabal new-build \
  --allow-newer \
  --allow-older \
  --disable-tests \
  --disable-benchmarks \
  --avoid-reinstalls \
  --dry-run \
  --only-configure \
  -f -external-libsodium-vrf \
  all

WORKDIR /usr/src
RUN rm *.txt
RUN plan2rpms.sh

FROM scratch AS exporter
COPY --from=solver \
  /usr/src/${APPLICATION}/plan*.json \
  ./

FROM solver AS builder

WORKDIR /usr/src/${APPLICATION}
RUN cabal new-build \
  --allow-newer \
  --allow-older \
  --disable-tests \
  --disable-benchmarks \
  --avoid-reinstalls \
  -f -external-libsodium-vrf \
  all