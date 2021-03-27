#!/bin/bash

set -e

GIT_ROOT=$(git rev-parse --show-toplevel)

OBS_CONFIG_PROJECTS_JSON_FILE="${GIT_ROOT}/obs/config/projects.json"

OBS_PRJ_STABLE=$(jq -r '.stable' < ${GIT_ROOT}/obs/config/projects.json)
OBS_PRJ_NIGHTLY=$(jq -r '.nightly' < ${GIT_ROOT}/obs/config/projects.json)

# Enable BuildKit for Docker
export DOCKER_BUILDKIT=1

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