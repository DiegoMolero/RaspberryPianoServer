#!/bin/bash
OUTPUT="$(amidi -l)" || sudo apt-get install amidi
if [[ $OUTPUT=*"MIDI"* ]]; then
        HOST="$(shuf -i 2000-2999 -n 1)"	#For Local Input
        python recive.py localhost $HOST &
        P1=$! &
        sleep .5
        amidi --port="hw:1,0,0" -d | nc localhost $HOST &
        P2=$!
        wait $P1 $P2
else
        echo "Connect the MIDI wire from the piano to the Raspberry"
fi



