#!/usr/bin/python
import os
import time
from subprocess import Popen, PIPE

tmp_dir="/tmp/"

class Playlist(object):
    pass

class Daemon(object):
    def __init__(self):
        self.current_file = "/home/liquuid/dog.flv"
        self.playing_now = "/home/liquuid/teste.avi"
        self.update_symlink()

    def update_symlink(self):
        os.system("ln -sf %s %s/video" % (self.playing_now, tmp_dir))

    def play(self):
        mplayer_cmd = "mplayer -fs -loop 0 -fixed-vo %s" % os.path.join(tmp_dir, 'video')

        while True:
            mplayer = Popen(mplayer_cmd.split(" "), stdout=PIPE)
            time.sleep(1)
            
            while mplayer.poll() is None: # mplayer rodando
                if 'Playing ' in mplayer.stdout.readline():
                    self.playing_now = self.current_file
                    self.update_symlink()
                else:
                    print "no no no"
                #print mplayer.poll()
                time.sleep(1)

p = Daemon()
p.play()
