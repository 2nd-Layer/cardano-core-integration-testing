#!/bin/bash

set -e

if [ -z "${GITHUB_WORKSPACE}" ]; then
  GITHUB_WORKSPACE=$(git rev-parse --show-toplevel)
fi
source "${GITHUB_WORKSPACE}/scripts/obs-core-functions.sh"

if ! which osc >/dev/null 2>&1; then
  echo "osc is not installed!"
  exit 2
fi

if [ ! -f ~/.oscrc ]; then
  echo '[general]' >> ~/.oscrc
  echo 'apiurl = https://api.opensuse.org' >> ~/.oscrc
  echo '' >> ~/.oscrc
  echo '[https://api.opensuse.org/]' >> ~/.oscrc
  echo 'realname = PERLUR OBS Automation' >> ~/.oscrc
  echo 'email = perlur.cloud@gmail.com' >> ~/.oscrc
  echo 'user=perlur-obs-automation' >> ~/.oscrc
  echo 'pass='${PERLUR_OBS_AUTOMATION_PASS} >> ~/.oscrc
fi

pushd ${GITHUB_WORKSPACE}/obs/cache/

if [ -d ${OBS_PRJ_STABLE} ]; then
  pushd ${OBS_PRJ_STABLE}
  clean_dirty_project
  osc_repair_wc
  osc up
  popd
else
  osc co ${OBS_PRJ_STABLE}
fi

if [ -d ${OBS_PRJ_NIGHTLY} ]; then
  pushd ${OBS_PRJ_NIGHTLY}
  clean_dirty_project
  osc_repair_wc
  osc up
  popd
else
  osc co ${OBS_PRJ_NIGHTLY}
fi 
