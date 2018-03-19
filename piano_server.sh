#!/bin/bash
OUTPUT="$(amidi -l)" || sudo apt-get install amidi
if [[ $OUTPUT=*"MIDI"* ]]; then
        LOCAL_PORT="$(shuf -i 2000-2999 -n 1)"	#For Local Input
		IP_ADDR="$(hostname -I | awk '{print $1}')"	#Taking IP Adrress for QR Code
        python recive_send.py $LOCAL_PORT &
        P1=$! &
        sleep .5
        amidi --port="hw:1,0,0" -d | nc localhost $LOCAL_PORT &
        P2=$! &
		python qr_show.py $IP_ADDR
        wait $P1 $P2
else
        echo "Connect the MIDI wire from the piano to the Raspberry Pi"
fi



