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

def clean_object(object_list):
    data = []
    for obj in object_list:
        temp = obj.__dict__
        temp.pop('_state')      
        data.append(temp)
            
    return data
    

def genre(request, genre_id=None):
    
    if genre_id:
        try:
            objs = clean_object(Genre.objects.get(id=genre_id).clip_set.all())
        except:
            return HttpResponse("")
    else:
        objs = clean_object(Genre.objects.all())
        
    return HttpResponse(json.dumps(objs))

def year(request, year_id=None):
    
    if year_id:
        try:
            objs = clean_object(Year.objects.get(id=year_id).clip_set.all())
        except:
            return HttpResponse("")
    else:
        objs = clean_object(Year.objects.all())
        
    return HttpResponse(json.dumps(objs))

def director(request, director_id=None):
    
    if director_id:
        try:
            objs = clean_object(Director.objects.get(id=director_id).clip_set.all())
        except:
            return HttpResponse("")
    else:
        objs = clean_object(Director.objects.all())
        
    return HttpResponse(json.dumps(objs))

def star(request, star_id=None):
    
    if star_id:
        try:
            objs = clean_object(Star.objects.get(id=star_id).clip_set.all())
        except:
            return HttpResponse("")
    else:
        objs = clean_object(Star.objects.all())
        
    return HttpResponse(json.dumps(objs))

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