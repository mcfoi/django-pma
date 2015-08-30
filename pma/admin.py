#from django.contrib import admin
from django.contrib.gis import admin as geoadmin
from models import Punto

geoadmin.site.register(Punto, geoadmin.GeoModelAdmin)
# Register your models here.
