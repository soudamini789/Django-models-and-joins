from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.
def insert_topic(request):
    n=input()
    to=topic.objects.get_or_create(topic_name=n)[0]
    to.save()
    return HttpResponse ('topic is created')

def insert_webpage(request):
    tn=input('topic_name is:')
    n=input('name is:')
    to=topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    wo=webpage.objects.get_or_create(topic_name=to,name=n)[0]
    wo.save()
    return HttpResponse ('webpage is created')
def insert_AccessRecords(request):
    tn=input('topic name is:')
    to=topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    n=input('name is:')
    wo=webpage.objects.get_or_create(topic_name=to,name=n)[0]
    wo.save()
    d=input('date is:')
    au=input('author is:')
    ao=AccessRecords.objects.get_or_create(name=wo,date=d,author=au)[0]
    ao.save()
    return HttpResponse ('accsess record is created')


