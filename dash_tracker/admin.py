IMPORT_EXPORT_USE_TRANSACTIONS = False

from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportActionModelAdmin
from django.conf import settings


# Register your models here.
from .models import Language, ProductTypeName, ProductGroupName, Mesurement, MesurementName, \
    Ingradient,IngradientName, Meal, MealName, ProductItem, Profile, ProductType, ProductGroup


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
admin.site.register(ProductItem)
admin.site.register(Profile)


class MesurementResource(resources.ModelResource):

    class Meta:
        model = Mesurement


# class MesurementAdmin(ImportExportModelAdmin):
#     resource_class = MesurementResource

#class MesurementAdmin(ImportExportActionModelAdmin):
#    pass