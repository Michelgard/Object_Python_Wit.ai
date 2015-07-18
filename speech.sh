#!/bin/bash
say() { 
local IFS=+
mpg123 -a hw:1,0 "http://translate.google.com/translate_tts?tl=fr&q=$*"
} 
say $*
