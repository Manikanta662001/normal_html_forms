from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['to']
        To=Topic.objects.get_or_create(topic_name=tn)[0]
        To.save()
        return HttpResponse('Topic Inserted successfully')
    return render(request,'insert_topic.html')
def insert_webpage(request):
    topics=Topic.objects.all()
    d={'topics':topics}
    if request.method=='POST':
        tn=request.POST['topic']
        name=request.POST['na']
        url=request.POST['ur']
        email=request.POST['em']
        T=Topic.objects.get_or_create(topic_name=tn)[0]
        T.save()
        Wo=Webpage.objects.get_or_create(topic_name=T,name=name,url=url,email=email)[0]
        Wo.save()
        return HttpResponse('Webpage Inserted successfully')
    return render(request,'insert_webpage.html',d)



def retrieve_data(request):
    LTO=Topic.objects.all()
    d={'topics':LTO}
    if request.method=='POST':
        td=request.POST.getlist('topic')
        print(td)
        webqueryset=Webpage.objects.none()

        for i in td:
            webqueryset=webqueryset|Webpage.objects.filter(topic_name=i)
        d1={'webpages':webqueryset}
        return render(request,'display_webpage.html',d1)
    return render(request,'retrieve_data.html',d)

def checkbox(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    return render(request,'checkbox.html',d)