from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
from django.db.models.functions import Length


def display_table(request):
    to=Topic.objects.all()
    d={'games':to}
    return render(request,'display_topic.html',context=d)

def display_webpage(request):
    wo=webpage.objects.all()
    wo=webpage.objects.filter(game_name='cricket')
    #wo=webpage.objects.get(game_name='chess')
    wo=webpage.objects.exclude(game_name='cricket')
    wo=webpage.objects.all()[1:4:]
    wo=webpage.objects.all().order_by('name')
    wo=webpage.objects.all().order_by('-name')

    wo=webpage.objects.all().order_by(Length('name'))
    wo=webpage.objects.all().order_by(Length('name').desc())
    wo=webpage.objects.filter(name__startswith='r')
    wo=webpage.objects.filter(email__endswith='.com')
    wo=webpage.objects.filter(name__contains='a')
    wo=webpage.objects.filter(name__in=('Dhoni','vishwa'))

    wo=webpage.objects.all()

    d={'web':wo}
    return render(request,'display_webpage.html',d)

def display_access(request):
    ao=acessrecord.objects.all()
    d={'access':ao}
    return render (request,'display_access.html',d)

def update_webpage(request):
    webpage.objects.filter(game_name='vollyball').update(name='sai')
    to=Topic.objects.get_or_create(game_name='cricket')[0]
    to.save()
    webpage.objects.update_or_create(name='Raina',defaults={'pno':7,'game_name':to,'url':'http://raina.com','email':'raina@gmail.in'})
    d={'web':webpage.objects.all()}
    return render(request,'display_webpage.html',d)