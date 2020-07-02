from django.shortcuts import render, HttpResponse
from .models import Project

# Create your views here.
def portfolio(request):
    try:
        projects = Project.objects.all()     
        return render(request, "portafolio/portafolio.html", {'projects':projects})
    except:
        import sys
        return HttpResponse(sys.exc_info())