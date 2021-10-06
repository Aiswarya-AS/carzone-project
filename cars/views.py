from django.shortcuts import get_object_or_404, render
from .models import car
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
# Create your views here.
def cars(request):
    cars = car.objects.order_by("-created_date")
    paginator  = Paginator(cars,1)
    page  = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    model_search = car.objects.values_list('model',flat=True).distinct()
    state_search = car.objects.values_list('state',flat=True).distinct()
    year_search = car.objects.values_list('year',flat=True).distinct()
    style_search = car.objects.values_list('body_style',flat=True).distinct()
    return render(request,'cars/cars.html',{
        "cars":paged_cars,
        "model_search":model_search,
        "state_search":state_search,
        "year_search":year_search,
        "style_search":style_search,
    })


def car_detail(request,id):
    single_car = get_object_or_404(car,pk=id)
    return render(request,"cars/car_detail.html",{
        "single_car":single_car
    })


def search(request):
    cars = car.objects.order_by('-created_date')
    model_search = car.objects.values_list('model',flat=True).distinct()
    state_search = car.objects.values_list('state',flat=True).distinct()
    year_search = car.objects.values_list('year',flat=True).distinct()
    style_search = car.objects.values_list('body_style',flat=True).distinct()
    transmission_search = car.objects.values_list('transmission',flat=True).distinct()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(description__icontains =keyword)

    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            cars = cars.filter(model__iexact =model)

    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            cars = cars.filter(state__iexact =state)
    

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            cars = cars.filter(year__iexact =year)


    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            cars = cars.filter(body_style__iexact =body_style)
    

    # if 'min_price' in request.GET:
    #     min_price = request.GET['min_price']
    #     max_price = request.GET['max_price']
    #     if max_price:
    #         cars = cars.filter(price__gte=min_price,price__lte=max_price)

    

    return render(request,'cars/search.html',{
        "cars":cars,
        "model_search":model_search,
        "state_search":state_search,
        "year_search":year_search,
        "style_search":style_search,
        'transmission_search':transmission_search,
    })