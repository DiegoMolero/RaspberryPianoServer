#!/bin/bash
OUTPUT="$(amidi -l)" || sudo apt-get install amidi
if [[ $OUTPUT = *"MIDI"* ]]; then
	var_random = $((RANDOM%1100+1000))
	echo var_random
else
	echo "Connect the MIDI wire from the piano to the Raspberry"
fi