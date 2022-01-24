from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    mobile_no = models.CharField(max_length=12)
    email = models.EmailField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField(null=True, blank=True)
