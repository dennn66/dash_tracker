from django.db import models
# from django.conf import settings
#from django.utils import timezone
from datetime import date
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

# class MouseEvent(models.Model):
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     x = models.IntegerField()
#     y = models.IntegerField()
#     event =  models.TextField()
#     event_date = models.DateTimeField(default=timezone.now)
#
#     def publish(self):
#         self.event_date = timezone.now()
#         self.save()
#
#     def __str__(self):
#         return self.event

class Language(models.Model):
    name = models.TextField()
    short_name = models.TextField()

    def __str__(self):
        return self.short_name

class ProductType(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name

class ProductTypeName(models.Model):
    name = models.TextField()
    lang = models.ForeignKey(Language, on_delete=models.CASCADE)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ProductGroup(models.Model):
    name = models.TextField()
    product_type =  models.ForeignKey(ProductType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ProductGroupName(models.Model):
    name = models.TextField()
    lang = models.ForeignKey(Language, on_delete=models.CASCADE)
    product_group = models.ForeignKey(ProductGroup, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Mesurement(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name

class MesurementName(models.Model):
    name = models.TextField()
    short_name = models.TextField()
    lang = models.ForeignKey(Language, on_delete=models.CASCADE)
    mesurement = models.ForeignKey(Mesurement, on_delete=models.CASCADE)

    def __str__(self):
        return self.short_name


class Ingradient(models.Model):
    name = models.TextField()
    product_group = models.ForeignKey(ProductGroup, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=5, decimal_places=2)
    mesurement = models.ForeignKey(Mesurement, on_delete=models.CASCADE)
    portions = models.DecimalField(max_digits=4, decimal_places=1)

    calories = models.IntegerField()#Calories
    calories_fat = models.DecimalField(max_digits=6, decimal_places=3)#Calories from Fat    Amount
    total_fat = models.DecimalField(max_digits=6, decimal_places=3)#Total Fat, g
    saturated_fat =  models.DecimalField(max_digits=6, decimal_places=3)#Saturated Fat, g
    monosaturated_fat  = models.DecimalField(max_digits=6, decimal_places=3)#Monounsaturated  Fat, g
    polyunsaturated_fat = models.DecimalField(max_digits=6, decimal_places=3)#Polyunsaturated  Fat, g
    cholestreol = models.DecimalField(max_digits=6, decimal_places=3)#Cholestreol, mg
    sodium = models.DecimalField(max_digits=6, decimal_places=3)#Sodium, mg
    potassium = models.DecimalField(max_digits=6, decimal_places=3)#Potassium, mg
    total_carbohydrate = models.DecimalField(max_digits=6, decimal_places=3)#Total Carbohydrate, g
    dietary_fiber = models.DecimalField(max_digits=6, decimal_places=3)#Dietary Fiber, g
    sugars = models.DecimalField(max_digits=6, decimal_places=3)#Sugars, g
    protein = models.DecimalField(max_digits=6, decimal_places=3)#Protein, g
    calcium = models.DecimalField(max_digits=6, decimal_places=3)#Calcium, mg
    iron = models.DecimalField(max_digits=6, decimal_places=3)#Iron, mg

    def __str__(self):
        return self.name


class IngradientName(models.Model):
    name = models.TextField()
    lang = models.ForeignKey(Language, on_delete=models.CASCADE)
    ingradient = models.ForeignKey(Ingradient, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Meal(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name

class MealName(models.Model):
    name = models.TextField()
    lang = models.ForeignKey(Language, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ProductItem(models.Model):
    date = models.DateField(default=date.today)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    ingradient = models.ForeignKey(Ingradient, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=5, decimal_places=2)
    mesurement = models.ForeignKey(Mesurement, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.ingradient)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    lang = models.ForeignKey(Language, on_delete=models.CASCADE, default=None)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        print('created')
        lang =  Language.objects.filter(short_name = 'en')
        if not lang:
            lang = Language.objects.create(name='english', short_name = 'en')
        Profile.objects.create(user=instance, lang = lang)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()