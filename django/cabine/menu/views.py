import os
import json
import operator
from datetime import datetime
from menu.models import *
from django.shortcuts import render_to_response
from django.http import HttpResponse

FIFO = "/tmp/fifo"

def index(request):
    clips = Clip.objects.all()
    
    for clip in clips:
        clip.verifica_capa()
    
    director_d = sortHash(movieHash(Director))
    genre_d = sortHash(movieHash(Genre))
    country_d = sortHash(movieHash(Country))
    star_d = sortHash(movieHash(Star))
    
    if os.path.exists("/tmp/waiting"):
        os.unlink("/tmp/waiting")
    
    return render_to_response('index.html', locals())

def movieHash(classe):
    hash = {}
    for item in clean_object(classe.objects.all()):
        hash[item["name"]] = clean_object(classe.objects.get(id=item["id"]).clip_set.all())
        
    return hash

def sortHash(hash):    
    lista = sorted(hash.iteritems(), key=operator.itemgetter(1))
    lista.sort()
    return lista

def countdown(request):
    os.system("echo 'loadfile /home/cabine/COUNTDOWN.mp4' > %s" % FIFO)
    return HttpResponse(True)

def enqueue(request, clip_id):
    clip = Clip.objects.get(id=clip_id)
    clip.count += 1
    clip.save()
    entry = Log(clip=clip,date=datetime.now())
    entry.save()
    #os.system("echo 'loadfile %s/%s.mp4' > %s" % ("/home/cabine/Videos/", clip_id  , FIFO))
    os.system("echo \"/home/cabine/COUNTDOWN.mp4\n %s/%s.mp4\" > /tmp/list" % ("/home/cabine/Videos/", clip_id))
    os.system("echo 'loadlist /tmp/list' > %s" %  FIFO)

    os.system("echo 'vo_fullscreen 1' > %s" % FIFO)
    os.system("touch /tmp/waiting")
    
    return HttpResponse(True)

def status(request):
    if not settings.PRODUCAO:
        return HttpResponse("idle")
    
    if os.path.exists(FIFO) and os.path.isfile(FIFO):
        os.unlink(FIFO)
        os.mkfifo(FIFO)
    
    if not os.path.exists(FIFO):
        os.mkfifo(FIFO)

    os.system("echo 'get_file_name' > %s" % FIFO)
    os.system("echo 'vo_fullscreen 1' > %s" % FIFO)
    log_line = open("/tmp/mplayer.log","r").read().split('\n')[-2]

    if "ANS_FILENAME=" in log_line:
        if os.path.exists("/tmp/waiting"):
            os.unlink("/tmp/waiting")

        return HttpResponse("playing %s " % log_line.split("=")[1])
    else:
        if os.path.exists("/tmp/waiting"):
            return HttpResponse("waiting")
        else:
            return HttpResponse("idle")

def clear_waiting(request):    
    if os.path.exists("/tmp/waiting"):
        os.unlink("/tmp/waiting")
    return HttpResponse(True)
    


def clean_object(object_list):
    data = []
    for obj in object_list:
        temp = obj.__dict__
        temp.pop('_state')      
        data.append(temp)
    return data
    
