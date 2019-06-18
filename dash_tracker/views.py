from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from .models import MouseEvent
from django.contrib.auth.decorators import login_required

@login_required
def event_list(request):
    events = MouseEvent.objects.order_by('event_date')
    return render(request, 'dash_tracker/event_list.html', {'events': events})

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


