from django.shortcuts import render
from forums.models import Forum,Events
# Create your views here.

def home(request):
    if request.user.is_authenticated:
        forums = request.user.forums.all()
        events = Events.objects.filter(forum__in=forums)
        context={'forums':forums,'events':events,}
        return render(request,'home.html',context)
    else:
        return render(request,'login.html')