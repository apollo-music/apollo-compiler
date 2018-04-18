#!/bin/bash
python3 start.py $1
python2 intermediate.py

MID_FILE="${1%.*}.mid"
MP3_FILE="${1%.*}.mp3"

timidity $MID_FILE -Ow -o - | lame - -b 64 $MP3_FILE