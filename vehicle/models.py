from django.db import models
from django.utils.translation import gettext_lazy as _

class VehicleCategory(models.TextChoices):
    BIKE = 'BI', _('Bike')
    CYCLE = 'CY', _('Cycle')
    CAR = 'CA', _('Car')
    BOAT = 'BO', _('Boat')

class Vehicle(models.Model):

    name = models.CharField(max_length=250)
    model_no = models.CharField(max_length=100)
    category = models.CharField(
        max_length=2,
        choices=VehicleCategory.choices
    )
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(null=True, blank=True)

    @property
    def categoryName(self):
        return VehicleCategory(self.category).name
