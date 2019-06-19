from django.contrib import admin

# Register your models here.
from .models import Language, ProductTypeName, ProductGroupName, Mesurement, MesurementName, \
    Ingradient,IngradientName, Meal, MealName, OnTheDish, Profile, ProductType, ProductGroup


admin.site.register(Language)
admin.site.register(ProductTypeName)
admin.site.register(ProductGroupName)
admin.site.register(ProductType)
admin.site.register(ProductGroup)
admin.site.register(Mesurement)
admin.site.register(MesurementName)
admin.site.register(Ingradient)
admin.site.register(IngradientName)
admin.site.register(Meal)
admin.site.register(MealName)
admin.site.register(OnTheDish)
admin.site.register(Profile)
