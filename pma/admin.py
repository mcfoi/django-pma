from django.contrib import admin
from django.contrib.gis import admin as geoadmin
from models import Punto, Sito

# Register your geo-models here.
geoadmin.site.register(Punto, geoadmin.GeoModelAdmin)
# Register your models here.
admin.site.register(Sito, admin.ModelAdmin)
