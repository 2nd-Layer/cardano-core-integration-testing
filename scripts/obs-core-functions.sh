#!/bin/bash

set -e

if [ -z "${GITHUB_WORKSPACE}" ]; then
  GITHUB_WORKSPACE=$(git rev-parse --show-toplevel)
fi

OBS_CONFIG_PROJECTS_JSON_FILE="${GITHUB_WORKSPACE}/obs/config/projects.json"

OBS_PRJ_STABLE=$(jq -r '.stable' < "${GITHUB_WORKSPACE}/obs/config/projects.json")
OBS_PRJ_NIGHTLY=$(jq -r '.nightly' < "${GITHUB_WORKSPACE}/obs/config/projects.json")


OBS_CONFIG_PROJECTS_JSON_FILE="${GITHUB_WORKSPACE}/obs/config/projects.json"

OBS_PRJ_STABLE=$(jq -r '.stable' < "${GITHUB_WORKSPACE}/obs/config/projects.json")
OBS_PRJ_NIGHTLY=$(jq -r '.nightly' < "${GITHUB_WORKSPACE}/obs/config/projects.json")

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
  for dir in $(ls); do
    osc repairwc ${dir}
  done
}