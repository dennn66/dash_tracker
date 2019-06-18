from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class MouseEvent(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    x = models.IntegerField()
    y = models.IntegerField()
    event =  models.TextField()
    event_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.event_date = timezone.now()
        self.save()

    def __str__(self):
        return self.event
