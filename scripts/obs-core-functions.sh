#!/bin/bash

set -e

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