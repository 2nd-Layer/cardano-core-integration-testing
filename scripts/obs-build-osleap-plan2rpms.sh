#!/bin/bash

set -e

if [ -z "${GITHUB_WORKSPACE}" ]; then
  GITHUB_WORKSPACE=$(git rev-parse --show-toplevel)
fi
source "${GITHUB_WORKSPACE}/scripts/obs-core-functions.sh"

echo 'Build openSUSE Leap plan2rpms Docker image'
pushd docker/openSUSE/Leap/15.3/

docker build \
  --pull \
  --tag osleap-plan2rpms \
  ./