from django.shortcuts import get_object_or_404, render
from .models import car
# Create your views here.
def cars(request):
    cars = car.objects.order_by("-created_date")
    paginator  = paginator(cars,1)
    page  = request.GET.get('page')
    
    return render(request,'cars/cars.html',{
        "cars":cars
    })


def car_detail(request,id):
    single_car = get_object_or_404(car,pk=id)
    return render(request,"cars/car_detail.html",{
        "single_car":single_car
    })