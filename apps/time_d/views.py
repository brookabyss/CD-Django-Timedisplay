from django.shortcuts import render,HttpResponse
import datetime

def index(request):
    time_now=datetime.datetime.now()
    time_now=time_now - datetime.timedelta(hours=7)
    context={
    "current_time": time_now.strftime('%Y-%m-%d %H:%M %p')
    }
    return render(request,'time_d/index.html', context)
