from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from .models import Language, ProductTypeName, ProductGroupName, Mesurement, MesurementName, \
    Ingradient,IngradientName, Meal, MealName, OnTheDish, Profile

from django.contrib.auth.decorators import login_required

@login_required
def dish(request):
    user = request.user
    prof = Profile.objects.get(user = user)
    lang = prof.lang
    ingradient_names = IngradientName.objects.filter(lang=lang)

    products = OnTheDish.objects.raw('SELECT * FROM ingradient LEFT OUTER JOIN (SELECT * FROM ingradientname WHERE ingradientname.lang = lang) AS ingradientname ON ingradientname.id = ingradient.id')

    print(lang)

    lname = lang.short_name
    print(lname)
    return render(request, 'dash_tracker/dish.html', {'products': products, 'lang' : lang})

# @login_required
# def camera(request):
#     return render(request, 'camera/camera.html', {})
#
#
# @login_required
# def mouse_event(request):
#     mouse_event = MouseEvent()
#     mouse_event.x  = request.GET['x']
#     mouse_event.y = request.GET['y']
#     mouse_event.event =  request.GET['event']
#     mouse_event.author = request.user
#     mouse_event.event_date = timezone.now()
#     mouse_event.save()
#     return render(request, 'camera/mouse_event.html', {'x': mouse_event.x, 'y' : mouse_event.y, 'event' : mouse_event.event})


