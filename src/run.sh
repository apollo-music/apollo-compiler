#!/bin/bash
python3 start.py $1
python2 intermediate.py
# Precisa achar o arquivo .mid gerado pelo intermediate e converter para mp3 com o comando abaixo
# timidity my_midi_file.mid -Ow -o - | lame - -b 64 my_converted_midi.mp3
