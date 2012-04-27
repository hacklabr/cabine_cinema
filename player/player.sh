#!/bin/bash
rm -rf /tmp/fifo
rm -rf /tmp/waiting

mkfifo /tmp/fifo
export DISPLAY=:0.1
mplayer ~/COUNTDOWN.mp4 -fs -quiet -idle -fixed-vo -monitoraspect 16:9 -slave -input file=/tmp/fifo > /tmp/mplayer.log
