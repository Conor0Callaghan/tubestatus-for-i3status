#!/bin/sh

# Shell script to prepend i3status with more stuff

i3status -c ~/.i3/i3status.conf | while :
do
	TEMP=`/bin/python3 ~/code/tubestatus.py --line=picadilly`

        read line
        echo "${TEMP} | $line" || exit 1
done
