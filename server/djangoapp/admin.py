from django.contrib import admin
from .models import CarMake, CarModel

# CarModelInline class

class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 3


# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    fields = ['car_make', 'name', 'type', 'year', 'dealer_id']
    list_display = ('car_make', 'name', 'type', 'year', 'dealer_id')
    list_filter = ['car_make', 'name', 'type', 'year', 'dealer_id']
    search_fields = ['car_make', 'name', 'type', 'year', 'dealer_id']


# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    fields = ['name', 'description']
    list_display = ('name', 'description')
    list_filter = ['name']
    search_fields = ['name', 'description']


# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
