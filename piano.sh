#!/bin/bash
OUTPUT="$(amidi -l)" || sudo apt-get install amidi
if [[ $OUTPUT = *"MIDI"* ]]; then
        python recive.py localhost "$(shuf -i 2000-2999 -n 1)"        #For input
        echo "$(shuf -i 3000-3999 -n 1)"        #For output

else
        echo "Connect the MIDI wire from the piano to the Raspberry"
fi

