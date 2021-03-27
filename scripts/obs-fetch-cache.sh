#!/bin/bash

set -e

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

OBS_PRJ_STABLE=$(jq -r '.stable' < obs/config/projects.json)
OBS_PRJ_NIGHTLY=$(jq -r '.nightly' < obs/config/projects.json)

function clean_dirty_project() {
  for dir in $(ls); do
    if [ ! -f ${dir}/*.spec ]; then
      rm -rf ${dir}
    fi
  done
}

function osc_repair_wc() {
for dir in `ls`; do
  osc repairwc ${dir}
done
}

pushd obs/cache/

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
