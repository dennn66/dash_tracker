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
    lang = prof.lang_id
    ingradient_names = IngradientName.objects.filter(lang=lang)

    products = OnTheDish.objects.raw('SELECT * FROM dash_tracker_ingradient LEFT OUTER JOIN (SELECT name AS ingradient_name, id FROM dash_tracker_ingradientname WHERE dash_tracker_ingradientname.lang_id = (SELECT lang_id FROM dash_tracker_profile WHERE user_id = %s)) AS dash_tracker_ingradientname ON dash_tracker_ingradientname.id = dash_tracker_ingradient.id', [request.user.id])

    # products = OnTheDish.objects.raw('(SELECT * FROM dash_tracker_ingradient LEFT OUTER JOIN '+
    #                                  '(SELECT name AS ingradient_name, id '+
    #                                  'FROM dash_tracker_ingradientname '+
    #                                  'WHERE dash_tracker_ingradientname.lang_id = ('+
    #                                  'SELECT lang_id FROM dash_tracker_profile '+
    #                                  'WHERE user_id = %s)) '+
    #                                  'AS dash_tracker_ingradientname '+
    #                                  'ON dash_tracker_ingradientname.id = dash_tracker_ingradient.id) '+
    #                                  'LEFT OUTER JOIN ('+
    #                                  'SELECT name '+
    #                                  'AS mesurement_name, id '+
    #                                  'FROM dash_tracker_mesurementname '+
    #                                  'WHERE dash_tracker_mesurementname.lang_id = ('+
    #                                  'SELECT lang_id '+
    #                                  'FROM dash_tracker_profile '+
    #                                  'WHERE user_id = %s)) '+
    #                                  'AS dash_tracker_mesurementname '+
    #                                  'ON dash_tracker_mesurementname.id = dash_tracker_ingradient.mesurement_id',
    #                                  [request.user.id, request.user.id])


    return render(request, 'dash_tracker/dish.html', {'products': products})

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


