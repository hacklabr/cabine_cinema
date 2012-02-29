from menu.models import *
from django.shortcuts import render_to_response

def index(request):
    clips = Clip.objects.all()

    return render_to_response('index.html', locals())
