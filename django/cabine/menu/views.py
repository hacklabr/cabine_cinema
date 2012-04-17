import os
import json
import operator

from menu.models import *
from django.shortcuts import render_to_response
from django.http import HttpResponse


def index(request):
    clips = Clip.objects.all()
    director_d = sortHash(movieHash(Director))
    genre_d = sortHash(movieHash(Genre))
    #import pdb;pdb.set_trace()
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

# TODO: remover
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
    
# TODO: remover
def genre(request, genre_id=None):
    
#    if genre_id:
#        try:
#            objs = clean_object(Genre.objects.get(id=genre_id).clip_set.all())
#        except:
#            return HttpResponse("")
#    else:
#        objs = clean_object(Genre.objects.all())

    genre_d = {}
    for genre in clean_object(Genre.objects.all()):
        #import pdb;pdb.set_trace()
        genre_d[genre["name"]] = clean_object(Genre.objects.get(id=genre["id"]).clip_set.all())
             
    return HttpResponse(json.dumps(genre_d))


# TODO: remover
def year(request, year_id=None):
    
    if year_id:
        try:
            objs = clean_object(Year.objects.get(id=year_id).clip_set.all())
        except:
            return HttpResponse("")
    else:
        objs = clean_object(Year.objects.all())
        
    return HttpResponse(json.dumps(objs))
# TODO: remover
def director(request, director_id=None):
    
    if director_id:
        try:
            objs = clean_object(Director.objects.get(id=director_id).clip_set.all())
        except:
            return HttpResponse("")
    else:
        objs = clean_object(Director.objects.all())
        
    return HttpResponse(json.dumps(objs))
# TODO: remover
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