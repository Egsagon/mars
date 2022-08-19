#!/usr/bin/sh

# Start picom
picom --experimental-backends &

# Start dunst
killall -9 dunst
dunst &

# Open eww widgets
eww open-many bar desk

# Start bain
/home/egsagon/.bain/bain mars &

# Start flashfocus
flashfocus &