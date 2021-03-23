#!/bin/bash

set -e

PLAN_JSON=$(find -name plan.json)

DEPS_COUNT=$(jq '."install-plan" | length' < ${PLAN_JSON})

for foo in `seq 0 $(($DEPS_COUNT-1))`; do
  PKG=`jq '."install-plan"['$foo']' < ${PLAN_JSON}`
  PKG_STYLE=`echo $PKG | jq '.style'`
  if [ "$PKG_STYLE" = '"global"' ]; then
    echo $PKG | jq '."pkg-name"' | sed -e 's/^"//' -e 's/"$//' >> hackage-dependencies.txt
  elif [ "$PKG_STYLE" = '"local"' ]; then
    echo $PKG | jq '."pkg-name"' | sed -e 's/^"//' -e 's/"$//' >> local-dependencies.txt
  else
    true
  fi
done

sort hackage-dependencies.txt | uniq > hackage-dependencies.txt.tmp
mv hackage-dependencies.txt.tmp hackage-dependencies.txt

while read -r line; do
  if ZYPP_INFO=`zypper search -x ghc-$line-devel`; then
    echo ghc-$line-devel >> installable-hackage-dependencies.txt
  elif ZYPP_INFO=`zypper search -x $line`; then
    echo $line >> installable-hackage-dependencies.txt
  else
    echo $line >> missing-hackage-dependencies.txt
  fi
done < hackage-dependencies.txt