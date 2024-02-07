from django.db import models

'''
Category
-----------------
title
---------------

Make
title
----------------------

Model
title
---------------------
=========================================
Auto
----------

Passenger cars
-----------------
#category, #make, #model, body, year, #price, #is_trade, engine_capacity, 
fuel_type, transmission, mileage, color, 
paint_type, drive, outside, optics, salon, media, options, additional,
#description, #photos, #region, #city, #phone_number
----------------------------------------------

Motor vehicles
--------------------------
#3category, technic_type, #make, #model, year,
#price, #is_trade, #description, #photos, #region, #city, #phone_number
-----------------------

Water transport
-----------------------
category, what_selling, 
price, is_trade, description, photos, region, city, phone_number

------------------------------------


====================================================
====================================================

Car's Part
--------------------------------
Part
------------------------
title, price, is_trade, category, make, model, status, delivery, part_type, 
description, photo, region, city, phone_number,

ConsAndOil
-------------------------------
category, title, price, is_trade, status, delivery,
description, photo, region, city, phone_number,

Accessories and electronics
-----------------------------------------
category, title, price, is_trade, status, delivery,
description, photo, region, city, phone_number,

Tire
--------------------------------------------------
category, title, price, is_trade, status, delivery, seasonality, 
diameter, width, profile, 
description, photo, region, city, phone_number,

Disk
--------------------------
category, title, price, is_trade, status, delivery,
type, diameter, 
description, photo, region, city, phone_number,
-----------------------------------

CarForPart
-------------------------------
category, title, price, is_trade, make, model, statys, delivery,
description, photo, region, city, phone_number,
================================================================
================================================================
Special technic
Trucks
--------------------------------------
category, title, make, model, year, price, is_trade, fuel_type,  
description, photo, region, city, phone_number,
------------------------------------

Bus
---------------------------------------
category, title, make, model, year, price, is_trade, fuel_type,  
transmission, availability,number_of_seats, mileage, 
description, photo, region, city, phone_number,

SpecTechnic
----------------------------
category, technic_type, make, model, year, price, is_trade, fuel_type,
availability, 
description, photo, region, city, phone_number,

Part
--------------------------
category, make, title, availability, is_trade, price, 
description, photo, region, city, phone_number,

Rent
--------------------------
category, make, type, model, is_trade, 
description, photo, region, city, phone_number,
-------------------------------------

Service
-------------------------------
category, make, model, is_trade, 
description, photo, region, city, phone_number,

TireAdnDisk
------------------------------------
category, make, title, is_trade, 
description, photo, region, city, phone_number,
=======================================================
======================================================
Repairs and Services
-------------------------------------------

Repair
-----------------------
category, repair_type, title, is_trade, 
description, photo, region, city, phone_number,
---------------------------------------------

Service
-----------------------------------
category, service_type, title, is_trade,
description, photo, region, city, phone_number,

Tuning
--------------------------------
category, tuning_type, title, is_trade,
description, photo, region, city, phone_number,

Other
-----------------------
category, title, is_trade,
description, photo, region, city, phone_number,

'''


class CommonModel(models.Model):
    title = models.CharField(max_length=64, unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Photos(models.Model):
    photo = models.ImageField(upload_to='images/')

    def __str__(self):
        return f'Photos(pk={self.pk})'



# Passenger Cars
class Color(CommonModel):
    pass


class Outside(CommonModel):
    pass


class Optics(CommonModel):
    pass


class Salon(CommonModel):
    pass


class Media(CommonModel):
    pass


class Options(CommonModel):
    pass


class Addition(CommonModel):
    pass


class RentToBuy(models.Model):
    prepayment = models.CharField(max_length=32)
    rental_period = models.PositiveSmallIntegerField()
    pay_per_month = models.CharField(max_length=32)


class PreCategory(CommonModel):
    pass


class Category(CommonModel):

    title = models.CharField(max_length=64)
    pre_category = models.ForeignKey(PreCategory, on_delete=models.CASCADE,
                                     related_name='categories')

    def __str__(self):
        return self.title


class Make(CommonModel):
    pass


class Model(CommonModel):
    make = models.ForeignKey(Make, on_delete=models.CASCADE,
                             related_name='models', blank=True, null=True)


class Region(CommonModel):
    pass


class City(CommonModel):

    region = models.ForeignKey(Region, on_delete=models.CASCADE,
                               related_name='cities')

    def __str__(self):
        return f'{self.title}'


class BaseModel(models.Model):
    class TradeChoice(models.TextChoices):
        YES = 'YE', 'Ha'
        NO = 'NO', 'Yoq'

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.CharField(max_length=16)
    is_trade = models.CharField(max_length=2, choices=TradeChoice.choices,
                                default=TradeChoice.NO)
    description = models.CharField(max_length=75, blank=True, null=True)
    photos = models.ManyToManyField(Photos)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=13)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class PassengerCar(BaseModel):
    class Body(models.TextChoices):
        EXP1 = 'EXP1', 'Example 1'
        EXP2 = 'EXP2', 'Example 2'
        __empty__ = None

    class Fuel(models.TextChoices):
        EXP1 = 'EXP1', 'Example 1'
        EXP2 = 'EXP2', 'Example 2'
        __empty__ = None

    class Transmission(models.TextChoices):
        EXP1 = 'EXP1', 'Example 1'
        EXP2 = 'EXP2', 'Example 2'
        __empty__ = None

    class PaintCondition(models.TextChoices):
        EXP1 = 'EXP1', 'Example 1'
        EXP2 = 'EXP2', 'Example 2'
        __empty__ = None

    class Drive(models.TextChoices):
        EXP1 = 'EXP1', 'Example 1'
        EXP2 = 'EXP2', 'Example 2'
        __empty__ = None

    make = models.ForeignKey(Make, on_delete=models.CASCADE,
                             related_name='cars')
    model = models.ForeignKey(Model, on_delete=models.CASCADE,
                              related_name='cars')
    body = models.CharField(max_length=4, choices=Body.choices,
                            default=Body.__empty__, blank=True, null=True)

    year = models.CharField(max_length=4)
    engine_capacity = models.FloatField(blank=True, null=True)

    fuel_type = models.CharField(max_length=4, choices=Fuel.choices,
                                 default=Fuel.EXP1)
    transmission = models.CharField(max_length=4, choices=Transmission.choices,
                                    default=Transmission.EXP1)

    mileage = models.PositiveIntegerField(blank=True, null=True)
    color = models.ForeignKey(Color, on_delete=models.CASCADE,
                              related_name='cars', blank=True, null=True)
    rent_to_buy = models.ManyToManyField(RentToBuy,
                                         related_name='passenger_cars')

    paint_condition = models.CharField(max_length=4, choices=PaintCondition.choices,
                                       default=PaintCondition.EXP1, blank=True, null=True)
    drive = models.CharField(max_length=4, choices=Drive.choices,
                             default=Drive.__empty__, blank=True, null=True)

    outsides = models.ManyToManyField(Outside, related_name='cars')
    optics = models.ManyToManyField(Optics, related_name='cars')
    salon = models.ManyToManyField(Salon, related_name='cars')
    media = models.ManyToManyField(Media, related_name='cars')
    options = models.ManyToManyField(Options, related_name='cars')
    addition = models.ManyToManyField(Addition, related_name='cars')

    def __str__(self):
        return f'{self.make} {self.model}'


# Motor vehicles
class MotoVehicle(BaseModel):
    class TechnicType(models.TextChoices):
        EXP1 = 'EXP1', 'EXAMPLE 1'
        EXP2 = 'EXP2', 'EXAMPLE 2'

    technic_type = models.CharField(max_length=4, choices=TechnicType.choices,
                                    default=TechnicType.EXP2)
    make = models.ForeignKey(Make, on_delete=models.CASCADE,
                             related_name='moto_vehicles')
    model = models.CharField(max_length=75, blank=True, null=True)
    year = models.CharField(max_length=4)

    def __str__(self):
        return f'{self.make} {self.model}'


# Water transport
class WaterTransport(BaseModel):
    class TransportChoice(models.TextChoices):
        EXP1 = 'EXP1', 'EXAMPLE 1'
        EXP2 = 'EXP2', 'EXAMPLE 2'

    selling = models.CharField(max_length=4, choices=TransportChoice.choices,
                                    default=TransportChoice.EXP2)

    def __str__(self):
        return self.selling


# Car's Part
class CommonPartAndProduct(BaseModel):
    class Delivery(models.TextChoices):
        YES = 'YE', 'Yes'
        NO = 'NO', 'No'
        __empty__ = None

    class Condition(models.TextChoices):
        EXP1 = 'EXP1', 'EXAMPLE 1'
        EXP2 = 'EXP2', 'EXAMPLE 2'
        __empty__ = None

    title = models.CharField(max_length=75)
    condition = models.CharField(max_length=4, choices=Condition.choices,
                              default=Condition.__empty__)
    delivery = models.CharField(max_length=2, choices=Delivery.choices,
                                default=Delivery.__empty__)

    class Meta:
        abstract = True


# Auto parts and products
class PartType(CommonModel):
    pass


class Diameter(CommonModel):
    pass


class Width(CommonModel):
    pass


class Profile(CommonModel):
    pass


class Part(CommonPartAndProduct):
    make = models.ForeignKey(Make, on_delete=models.CASCADE,
                             related_name='car_parts')
    model = models.ForeignKey(Model, on_delete=models.CASCADE,
                              related_name='car_parts')
    part_type = models.ForeignKey(PartType, on_delete=models.CASCADE,
                                  related_name='car_parts')

    def __str__(self):
        return self.title


class ConsAndOil(CommonPartAndProduct):

    def __str__(self):
        return {self.title}


class AccessAndElect(CommonPartAndProduct):

    def __str__(self):
        return self.title


class Tire(CommonPartAndProduct):
    class Seasonality(models.TextChoices):
        EXP1 = 'EXP1', 'EXAMPLE 1'
        EXP2 = 'EXP2', 'EXAMPLE 2'
        __empty__ = None

    seasonality = models.CharField(max_length=4, choices=Seasonality.choices,
                                   default=Seasonality.__empty__)
    diameter = models.ForeignKey(Diameter, on_delete=models.CASCADE,
                                 related_name='tires')
    width = models.ForeignKey(Width, on_delete=models.CASCADE,
                              related_name='tires')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,
                                related_name='tires')


class Disk(CommonPartAndProduct):
    class DType(models.TextChoices):
        EXP1 = 'EXP1', 'EXAMPLE 1'
        EXP2 = 'EXP2', 'EXAMPLE 2'
        __empty__ = None

    d_type = models.CharField(max_length=4, choices=DType.choices,
                              default=DType.__empty__)
    diameter = models.ForeignKey(Diameter, on_delete=models.CASCADE,
                                 related_name='disks')


class CarForPart(CommonPartAndProduct):
    make = models.ForeignKey(Make, on_delete=models.CASCADE,
                             related_name='car_for_parts')
    model = models.ForeignKey(Model, on_delete=models.CASCADE,
                              related_name='car_for_parts')


# Special technics
class Truck(BaseModel):

    class Fuel(models.TextChoices):
        EXP1 = 'EXP1', 'Example 1'
        EXP2 = 'EXP2', 'Example 2'
        __empty__ = None

    make = models.ForeignKey(Make, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    year = models.CharField(max_length=4)
    fuel_type = models.CharField(max_length=4, choices=Fuel.choices,
                                 default=Fuel.EXP1)


class Bus(BaseModel):
    class Fuel(models.TextChoices):
        EXP1 = 'EXP1', 'Example 1'
        EXP2 = 'EXP2', 'Example 2'
        __empty__ = None

    class Transmission(models.TextChoices):
        EXP1 = 'EXP1', 'Example 1'
        EXP2 = 'EXP2', 'Example 2'
        __empty__ = None

    class Availability(models.TextChoices):
        EXP1 = 'EXP1', 'Example 1'
        EXP2 = 'EXP2', 'Example 2'
        __empty__ = None

    make = models.ForeignKey(Make, on_delete=models.CASCADE,
                             related_name='trucks')
    model = models.ForeignKey(Model, on_delete=models.CASCADE,
                              related_name='trucks')
    year = models.CharField(max_length=4)
    fuel_type = models.CharField(max_length=4, choices=Fuel.choices,
                                 default=Fuel.EXP1)
    transmission = models.CharField(max_length=4, choices=Transmission.choices,
                                 default=Transmission.EXP1)
    availability = models.CharField(max_length=4, choices=Availability.choices,
                                    default=Availability.EXP1)
    number_of_seats = models.PositiveIntegerField()
    mileage = models.PositiveIntegerField()


class TechnicType(CommonModel):
    pass


class SpecTechnic(BaseModel):
    class Fuel(models.TextChoices):
        EXP1 = 'EXP1', 'Example 1'
        EXP2 = 'EXP2', 'Example 2'
        __empty__ = None

    class Availability(models.TextChoices):
        EXP1 = 'EXP1', 'Example 1'
        EXP2 = 'EXP2', 'Example 2'
        __empty__ = None
    technic_type = models.ForeignKey(TechnicType, on_delete=models.CASCADE,
                                     related_name='spec_technics')
    make = models.ForeignKey(Make, on_delete=models.CASCADE)

    model = models.CharField(max_length=75, blank=True, null=True)
    year = models.CharField(max_length=4)
    fuel_type = models.CharField(max_length=4, choices=Fuel.choices,
                                 default=Fuel.EXP1)
    availability = models.CharField(max_length=4, choices=Availability.choices,
                                    default=Availability.EXP1)


class SpecTechnicPart(BaseModel):

    class Availability(models.TextChoices):
        EXP1 = 'EXP1', 'Example 1'
        EXP2 = 'EXP2', 'Example 2'
        __empty__ = None

    make = models.ForeignKey(Make, on_delete=models.CASCADE)
    title = models.CharField(max_length=75)
    availability = models.CharField(max_length=4, choices=Availability.choices,
                                    default=Availability.EXP1)


class Rent(BaseModel):
    class RType(models.TextChoices):
        EXP1 = 'EXP1', 'Example 1'
        EXP2 = 'EXP2', 'Example 2'
        __empty__ = None

    make = models.ForeignKey(Make, on_delete=models.CASCADE,
                             related_name='rents')
    r_type = models.CharField(max_length=4, choices=RType.choices,
                              default=RType.EXP1)
    model = models.CharField(max_length=64)


class ServiceCommercial(BaseModel):
    make = models.ForeignKey(Make, on_delete=models.CASCADE)
    model = models.CharField(max_length=64)


class TireAndDisk(BaseModel):
    make = models.ForeignKey(Make, on_delete=models.CASCADE)
    title = models.CharField(max_length=75)


# Repairs and Services
class Repair(BaseModel):

    class RType(models.TextChoices):
        XP1 = 'EXP1', 'EXAMPLE 1'
        EXP2 = 'EXP2', 'EXAMPLE 2'
        __empty__ = None

    title = models.CharField(max_length=75)
    r_type = models.CharField(max_length=4, choices=RType.choices,
                              default=RType.__empty__)


class Service(BaseModel):
    class SType(models.TextChoices):
        XP1 = 'EXP1', 'EXAMPLE 1'
        EXP2 = 'EXP2', 'EXAMPLE 2'
        __empty__ = None

    title = models.CharField(max_length=75)
    s_type = models.CharField(max_length=4, choices=SType.choices,
                              default=SType.__empty__)


class Tuning(BaseModel):
    class TType(models.TextChoices):
        XP1 = 'EXP1', 'EXAMPLE 1'
        EXP2 = 'EXP2', 'EXAMPLE 2'
        __empty__ = None

    title = models.CharField(max_length=75)
    t_type = models.CharField(max_length=4, choices=TType.choices,
                              default=TType.__empty__)


class Other(BaseModel):
    title = models.CharField(max_length=75)

