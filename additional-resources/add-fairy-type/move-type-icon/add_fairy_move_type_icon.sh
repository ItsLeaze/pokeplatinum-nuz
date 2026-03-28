#!/bin/bash

NARC_ORIGIN=../../../res/prebuilt/battle/graphic/pl_batt_obj.narc

~/.local/bin/narc x $NARC_ORIGIN
cp 00343.NCGR.lz ./pl_batt_obj.narc.d/
~/.local/bin/narc c ./pl_batt_obj.narc.d/
mv -f .narc $NARC_ORIGIN

echo "Done updating narc at ${NARC_ORIGIN}."
echo "Cleaning up..."

rm -r ./pl_batt_obj.narc.d/ || true

echo "Cleaned up."
