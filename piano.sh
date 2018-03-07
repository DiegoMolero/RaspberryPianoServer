#!/bin/bash
OUTPUT="$(amidi -l)" || sudo apt-get install amidi
echo "Output: ${OUTPUT}"
if [[ $OUTPUT = *"MIDI"* ]]; then
	echo "$OUTPUT"
else
	echo "Connect the MIDI wire from the piano to the Raspberry"
fi