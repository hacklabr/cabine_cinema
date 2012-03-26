from menu.models import *
from django.shortcuts import render_to_response
from django.http import HttpResponse
import os
import json

def index(request):
    clips = Clip.objects.all()
    clips_all = clips
    clips_year = clips.order_by('year')
    clips_director = clips.order_by('director')
    clips_genre = clips.order_by('genre')
    
    return render_to_response('index.html', locals())

def enqueue(request, clip_id):
    clip = Clip.objects.get(id=clip_id)
    #fd = open("/tmp/list.pls","w")
    #fd.write(clip.file_path)
    os.system("ln -sf %s /tmp/video" % clip.file_path)
    return HttpResponse(clip.file_path)

def clips(request, order=None):
    
    clips = []
    
    if order:
        objs = Clip.objects.all().order_by(order)
    else:
        objs = Clip.objects.all()

    for clip in objs:
        temp = clip.__dict__
        temp.pop('_state')      
        clips.append(temp)
            
    return HttpResponse(json.dumps(clips))