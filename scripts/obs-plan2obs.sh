#!/bin/bash

set -e

if [ -z "${GITHUB_WORKSPACE}" ]; then
  GITHUB_WORKSPACE=$(git rev-parse --show-toplevel)
fi
source "${GITHUB_WORKSPACE}/scripts/obs-core-functions.sh"

if [ -z "${APPLICATION}" ]; then
  APPLICATION="cardano-node"
else
  APPLICATION=${APPLICATION}
fi

if [ -z "${APPLICATION_VERSION}" ]; then
  APPLICATION_VERSION="master"
  OBS_PROJECT_NAME=$(jq -r '.nightly' < obs/config/projects.json)
else
  APPLICATION_VERSION=${APPLICATION_VERSION}
  OBS_PROJECT_NAME=$(jq -r '.stable' < obs/config/projects.json)
fi

echo "Generate plan.json for ${APPLICATION}"
echo "  Version: ${APPLICATION_VERSION}"

pushd packages/apps/${APPLICATION}/docker/

docker build \
  --build-arg APPLICATION=${APPLICATION} \
  --build-arg APPLICATION_VERSION=${APPLICATION_VERSION} \
  --output out/ \
  --target exporter \
  ./

if [ ! -d "${GITHUB_WORKSPACE}/packages/apps/${APPLICATION}/cabal-install-plans/${APPLICATION_VERSION}" ]; then
  mkdir -p "${GITHUB_WORKSPACE}/packages/apps/${APPLICATION}/cabal-install-plans/${APPLICATION_VERSION}/"
fi
mv out/plan*.json "${GITHUB_WORKSPACE}/packages/apps/${APPLICATION}/cabal-install-plans/${APPLICATION_VERSION}/"
rmdir out

docker build \
  --build-arg APPLICATION=${APPLICATION} \
  --build-arg APPLICATION_VERSION=${APPLICATION_VERSION} \
  ./

popd

pushd obs/cache/${OBS_PROJECT_NAME}

# Process plan.local.json
local_pkgs=$(jq -r 'map(."pkg-name") | unique | .[]' < "${GITHUB_WORKSPACE}/packages/apps/${APPLICATION}/cabal-install-plans/${APPLICATION_VERSION}/plan.local.json")
for pkg in ${local_pkgs}; do
  if [ ! -d "ghc-"${pkg} ]; then
    echo 'ghc-'${pkg}
    osc mkpac ${pkg}
    pushd ${pkg}
    popd
  fi
done
