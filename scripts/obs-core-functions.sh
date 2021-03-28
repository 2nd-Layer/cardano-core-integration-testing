#!/bin/bash

set -e

if [ -z "${GITHUB_WORKSPACE}" ]; then
  GITHUB_WORKSPACE=$(git rev-parse --show-toplevel)
fi

if [ ! -z "${DOCKER_APPLICATION}" ]; then
  APPLICATION=${DOCKER_APPLICATION}
fi

OBS_CONFIG_PROJECTS_JSON_FILE="${GITHUB_WORKSPACE}/obs/config/projects.json"

OBS_PRJ_STABLE=$(jq -r '.stable' < "${GITHUB_WORKSPACE}/obs/config/projects.json")
OBS_PRJ_NIGHTLY=$(jq -r '.nightly' < "${GITHUB_WORKSPACE}/obs/config/projects.json")

OBS_CONFIG_PROJECTS_JSON_FILE="${GITHUB_WORKSPACE}/obs/config/projects.json"

# Enable BuildKit for Docker
export DOCKER_BUILDKIT=1

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

function clean_dirty_project() {
  for dir in $(ls); do
    if [ ! -f ${dir}/*.spec ]; then
      rm -rf ${dir}
    fi
  done
}

function osc_repair_wc() {
  for dir in $(ls); do
    osc repairwc ${dir}
  done
}