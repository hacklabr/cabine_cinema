#!/bin/bash
rm -rf /tmp/fifo
rm -rf /tmp/waiting

mkfifo /tmp/fifo

mplayer ~/COUNTDOWN.mp4 -fs -quiet -idle -fixed-vo -slave -input file=/tmp/fifo > /tmp/mplayer.log
