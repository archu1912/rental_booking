from django.db import models
from customer.models import Customer
from vehicle.models import Vehicle
from django.utils.translation import gettext_lazy as _

class RentStatus(models.TextChoices):
    RENT = 'RN', _('Rent')
    RETURN = 'RE', _('Return')
    RETURN_DAMAGE = 'RD', _('Return Damage')


# Create your models here.
class Booking(models.Model):

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    rent_status = models.CharField(
        max_length=2,
        choices=RentStatus.choices
    )
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(null=True, blank=True)

    @property
    def statusName(self):
        return RentStatus(self.rent_status).name