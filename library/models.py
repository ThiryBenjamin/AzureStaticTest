from django.db import models
from django.db.models import IntegerField, Model
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Claim(models.Model):
    INCURRED = "Incurred"
    PAID = "Paid"
    OUTSTANDING = "Outstanding"
    TYPE_OF_CLAIM_CHOICE = [
        (INCURRED, "Incurred"),
        (PAID, "Paid"),
        (OUTSTANDING, "Outstanding"),
    ]
    claim_number = models.FileField(upload_to='library')
    year = models.IntegerField(
        default= 2000,
        validators=[
            MaxValueValidator(2023),
            MinValueValidator(1990),
        ]
    )
    type  = models.CharField(
        max_length= 12,
        choices=TYPE_OF_CLAIM_CHOICE,
        default=INCURRED
    )
    amount = models.FloatField()

    def __str__(self):
        return self.number