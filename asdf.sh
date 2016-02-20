#!/bin/bash

PROGNAME="StreetFighter2"

while true ; do
    c="$(cat command)"
    xdotool search --name "$PROGNAME" $c
done
