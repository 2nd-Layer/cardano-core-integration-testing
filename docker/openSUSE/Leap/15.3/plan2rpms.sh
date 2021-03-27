#!/bin/bash

set -e

export PLAN_ORIG_JSON=$(find $(pwd) -name plan.json)

cp ${PLAN_ORIG_JSON} plan.json

# Sub-select cabal-install plan to separate file
jq '."install-plan" | map(.)' < ${PLAN_ORIG_JSON} > plan.install.json
export PLAN_INSTALL_JSON="$(pwd)/plan.install.json"
INSTALL_DEPS_COUNT=$(jq '. | length' < ${PLAN_INSTALL_JSON})

# Sub-select global (Hackage) dependencies to separate file
jq '. | map( . | select(.style == "global"))' < ${PLAN_INSTALL_JSON} > plan.global.json
export PLAN_GLOBAL_JSON="$(pwd)/plan.global.json"
GLOBAL_DEPS_COUNT=$(jq '. | length' < ${PLAN_GLOBAL_JSON})

# Sub-select local (Git,...) dependencies to separate file
jq '. | map( . | select(.style == "local"))' < ${PLAN_INSTALL_JSON} > plan.local.json
export PLAN_LOCAL_JSON="$(pwd)/plan.local.json"
LOCAL_DEPS_COUNT=$(jq '. | length' < ${PLAN_LOCAL_JSON})

echo "Detected total of ${INSTALL_DEPS_COUNT} dependencies!"
echo "  Global dependencies: ${GLOBAL_DEPS_COUNT}"
echo "  Local dependencies: ${LOCAL_DEPS_COUNT}"
echo "Checksum: $((${GLOBAL_DEPS_COUNT}+${LOCAL_DEPS_COUNT}))"

jq 'map( ."pkg-name") | unique' < ${PLAN_GLOBAL_JSON} | jq -r .[] > hackage-dependencies.txt

jq 'map( ."pkg-name") | unique' < ${PLAN_LOCAL_JSON} | jq -r .[] > local-dependencies.txt

# This loop is quite slow
echo 'Looking up Hackage dependencies...'
while read -r line; do
  if ZYPP_INFO=`zypper search --not-installed-only -x ghc-$line-devel`; then
    echo "  Found package: ghc-$line-devel"
    echo ghc-$line-devel >> installable-hackage-dependencies.txt
  elif ZYPP_INFO=`zypper search --not-installed-only -x $line`; then
    echo "  Found package: $line"
    echo $line >> installable-hackage-dependencies.txt
  else
    echo "  Did not find package: $line"
    echo $line >> missing-hackage-dependencies.txt
  fi
done < hackage-dependencies.txt