from menu.models import *
from django.shortcuts import render_to_response
from django.http import HttpResponse
import os

def index(request):
    clips = Clip.objects.all()

    return render_to_response('index.html', locals())

def enqueue(request, clip_id):
    clip = Clip.objects.get(id=clip_id)
    #fd = open("/tmp/list.pls","w")
    #fd.write(clip.file_path)
    os.system("ln -sf %s /tmp/video" % clip.file_path)
    return HttpResponse(clip.file_path)

