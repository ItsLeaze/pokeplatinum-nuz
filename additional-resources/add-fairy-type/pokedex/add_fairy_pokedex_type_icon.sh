#!/bin/bash

NITROGFX_PATH=../../../../dev/nitrogfx/build
NARC_ORIGIN=../../../res/prebuilt/resource/eng/zukan/zukan.narc

~/.local/bin/narc x $NARC_ORIGIN
cp ./00013.NCLR ./zukan.narc.d/
cp ./00088.NCER.lz ./zukan.narc.d/
cp ./00089.NANR.lz ./zukan.narc.d/
cp ./00090.NCGR.lz ./zukan.narc.d/
~/.local/bin/narc c zukan.narc.d/
mv -f .narc $NARC_ORIGIN

echo "Done updating narc at ${NARC_ORIGIN}."
echo "Cleaning up..."

rm -r ./zukan.narc.d/ || true

echo "Cleaned up."
