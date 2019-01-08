#!/usr/bin/env bash 
# Contributor: Alex Craig

INPUTFILE="$1"
FILENAME="${INPUTFILE%.*}"

# 300 DPI grayscale tiff
gs -q -dNOPAUSE -dBATCH -sDEVICE=tiffg4  -r300 -sOutputFile="$FILENAME.tif" $INPUTFILE


