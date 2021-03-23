#!/bin/bash

set -e

if ! which osc >/dev/null 2>&1; then
  echo "osc is not installed!"
  exit 2
fi

OBS_PRJ_STABLE=$(jq -r '.stable' < obs/config/projects.json)
OBS_PRJ_NIGHTLY=$(jq -r '.nightly' < obs/config/projects.json)

pushd obs/cache/

if [ -d ${OBS_PRJ_STABLE} ]; then
  pushd ${OBS_PRJ_STABLE}
  osc up
  popd
else
  osc co ${OBS_PRJ_STABLE}
fi

if [ -d ${OBS_PRJ_NIGHTLY} ]; then
  pushd ${OBS_PRJ_NIGHTLY}
  osc up
  popd
else
  osc co ${OBS_PRJ_NIGHTLY}
fi