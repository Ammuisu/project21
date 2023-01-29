from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    tn=input("Enter Topic Name")
    T=Topic.objects.get_or_create(topic_name=tn)[0]
    T.save()
    return HttpResponse("topic is inserted successfully")

def insert_webpage(request):
    tn=input("Enter Topic Name")
    name=input("Enter Name")
    url=input("Enter url")
    T=Topic.objects.get_or_create(topic_name=tn)[0]
    T.save()
    W=Webpage.objects.get_or_create(topic_name=T,name=name,url=url)[0]
    W.save()
    return HttpResponse("Webpage is inserted")