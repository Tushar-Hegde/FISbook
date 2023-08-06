from django.shortcuts import render
from .models import Forum,Events,Notices
from datetime import datetime
# Create your views here.

def forum(request,forum_id):
    forum = Forum.objects.get(id=forum_id)
    events = Events.objects.filter(forum__id = forum_id)
    notices = Notices.objects.filter(forum__id=forum_id)
    context = {'forum':forum,'events':events,'notices':notices,}
    return render(request,'forum.html',context)