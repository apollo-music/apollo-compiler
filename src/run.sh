#!/bin/bash
python3 start.py $1
python2 intermediate.py
<<<<<<< HEAD

MID_FILE="${1%.*}.mid"
MP3_FILE="${1%.*}.mp3"

timidity $MID_FILE -Ow -o - | lame - -b 64 $MP3_FILE
=======
# Precisa achar o arquivo .mid gerado pelo intermediate e converter para mp3 com o comando abaixo
# timidity my_midi_file.mid -Ow -o - | lame - -b 64 my_converted_midi.mp3
>>>>>>> 324386b1a1ab3c9d99b9016ee55fe6c0bb4860a5
