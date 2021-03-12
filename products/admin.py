from django.contrib import admin
from .models import *

class BikeImagesLine(admin.TabularInline):
    model = BikeImages
    fields = ('image',)

@admin.register(Bike)
class BikeAdmin(admin.ModelAdmin):
    inlines = [BikeImagesLine,]

admin.site.register(Category)
admin.site.register(ColorVariant)
