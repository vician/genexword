GenExWord
=========

Generate exist word

Small script to generating random existing word.
Primary used for DrawSomething, if you cannot guess a picture.

This script generates all unique combination of input chars with selected length.
These combination are compared with system dictionary (to verify that randomly generated word exists).
This script also uses Google translator for translation to your native language.

Required:
	https://github.com/terryyin/google-translate-python

Usage:
./genexword listchars N
	listchars is list of availible char
	N is lenght of finding word

Example:
./genexword anzpwesq 4
