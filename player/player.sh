#!/bin/bash
rm -rf /tmp/fifo
mkfifo /tmp/fifo

mplayer dog.flv -quiet  -idle -fixed-vo -slave -input file=/tmp/fifo > /tmp/mplayer.log
