from django.db import models
from vehicle.models import Vehicle

# Create your models here.
class Inventory(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    inventory_qty = models.IntegerField()
    buffer_qty = models.IntegerField()
    damage_qty = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(null=True, blank=True)
