from django.urls import path
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from . import views
'''





'''
urlpatterns = [
    #path(r'what_ont_the_dish', views.dish, name='dish'),
    #path(r'camera', views.camera, name='camera'),
    path(r'', views.dish, name='dish'),
    #path(r'mouseevent', views.mouse_event, name='mouse_event'),
]

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns += staticfiles_urlpatterns()
