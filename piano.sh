#!/bin/bash
OUTPUT="$(amidi -l)" || sudo apt-get install amidi
echo "${OUTPUT}"