from pages.models import Team
from django.shortcuts import render
from cars.models import car
# Create your views here.
def home(request):
    teams = Team.objects.all()
    featured_cars = car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = car.objects.order_by('-created_date')
    # search_fields = car.objects.values('model','state','year','body_style')
    model_search = car.objects.values_list('model',flat=True).distinct()
    state_search = car.objects.values_list('state',flat=True).distinct()
    year_search = car.objects.values_list('year',flat=True).distinct()
    style_search = car.objects.values_list('body_style',flat=True).distinct()
    return render(request,'pages/home.html',{
        "teams":teams,
        "featured_cars":featured_cars,
        "all_cars":all_cars,
        # 'search_fields':search_fields,
        "model_search":model_search,
        "state_search":state_search,
        "year_search":year_search,
        "style_search":style_search
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