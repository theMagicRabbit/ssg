#!/bin/sh

~/.local/share/virtualenvs/ssg-3xlCM2Xs/bin/python3 ~/Documents/src/github/ssg/src/main.py
cd public && ~/.local/share/virtualenvs/ssg-3xlCM2Xs/bin/python3 -m http.server 8888

