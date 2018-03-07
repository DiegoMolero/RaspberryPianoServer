#!/bin/bash
OUTPUT="$(amidi -l)" || sudo apt-get install amidi
if [[ $OUTPUT = *"MIDI"* ]]; then
	echo "$OUTPUT"
else
	echo "Connect the MIDI wire from the piano to the Raspberry"
fi