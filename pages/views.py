from pages.models import Team
from django.shortcuts import render

# Create your views here.
def home(request):
    teams = Team.objects.all()
    return render(request,'pages/home.html',{
        "teams":teams
    })


def about(request):
    teams = Team.objects.all()
    return render(request,'pages/about.html',{
        "teams":teams
    })

def services(request):
    return render(request,'pages/services.html')

def contact(request):
    return render(request,'pages/contact.html')