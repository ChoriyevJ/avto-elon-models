from django.contrib import admin

from autoads import models


@admin.register(models.PassengerCar)
class PassengerCarsAdmin(admin.ModelAdmin):
    list_display = (
        'make', 'model', 'body', 'fuel_type', 'transmission',
        'mileage', 'color', 'paint_condition', 'drive',
    )
