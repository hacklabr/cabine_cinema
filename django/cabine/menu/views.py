import os
import json
import operator
from datetime import datetime
from menu.models import *
from django.shortcuts import render_to_response
from django.http import HttpResponse


def index(request):
    clips = Clip.objects.all()
    director_d = sortHash(movieHash(Director))
    genre_d = sortHash(movieHash(Genre))
    country_d = sortHash(movieHash(Country))
    star_d = sortHash(movieHash(Star))
    
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

def enqueue(request, clip_id):
    clip = Clip.objects.get(id=clip_id)
    clip.count += 1
    clip.save()
    entry = Log(clip=clip,date=datetime.now())
    entry.save()
    os.system("echo 'loadfile %s' > /tmp/fifo" % clip.file_path)

    return HttpResponse(True)

def status(request):
    os.system("echo 'get_file_name' > /tmp/fifo")
    log_line = open("/tmp/mplayer.log","r").read().split('\n')[-2]
    if "ANS_FILENAME=" in log_line:
        return HttpResponse("playing %s " % log_line.split("=")[1])
    else:
        return HttpResponse("idle")


def clean_object(object_list):
    data = []
    for obj in object_list:
        temp = obj.__dict__
        temp.pop('_state')      
        data.append(temp)
    return data
    
