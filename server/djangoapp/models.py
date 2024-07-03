from django.db import models
# from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class CarMake(models.Model):
    name = models.CharField(
        null=False,
        max_length=50,
        default=None,
    )
    description = models.TextField(
        null=False,
        max_length=1000,
        default=None,
    )

    # Create a toString method for the class for object string representation
    def __str__(self):
        return "Name: " + self.name + "," + \
               "Description: " + self.description


class CarModel(models.Model):
    # Many-To-One relationship to Car Make model
    # One Car Make has many Car Models, using ForeignKey field
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(
        null=False,
        max_length=50,
        default=None,
    )
    # Types
    COUPE = 'Coupe'
    HATCHBACK = 'Hatchback'
    MICRO = 'Micro'
    ROADSTER = 'Roadster'
    SEDAN = 'Sedan'
    SPORTCAR = 'Sportcar'
    SUV = 'SUV'
    PICKUP = 'Pickup'
    WAGON = 'WAGON'
    VAN = 'Van'
    # Type choices
    TYPE_CHOICES = [
        (COUPE, 'Coupe'),
        (HATCHBACK, 'Hatchback'),
        (MICRO, 'Micro'),
        (ROADSTER, 'Roadster'),
        (SEDAN, 'Sedan'),
        (SPORTCAR, 'Sportcar'),
        (SUV, 'SUV'),
        (PICKUP, 'Pickup'),
        (WAGON, 'WAGON'),
        (VAN, 'Van'),
    ]
    # Type (CharField with a choices argument to provide limited choices)
    type = models.CharField(
        null=False,
        max_length=50,
        choices=TYPE_CHOICES,
        default=None,
    )
    year = models.IntegerField(
        null=False,
        validators=[
            MinValueValidator(2000),
            MaxValueValidator(2025)
        ],
        default=2024,
    )
    dealer_id = models.IntegerField(
        null=True,
        default=None,
    )
