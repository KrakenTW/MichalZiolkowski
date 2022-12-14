from django.contrib.auth.models import User
from django.db import models

from providers.models import Provider


CATEGORY_CHOICES = [
    ('Barber', 'Barber'), 
    ('Kosmetyczka', 'Kosmetyczka')
]


class Service(models.Model):
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=1024)
    category = models.CharField(max_length=64, choices=CATEGORY_CHOICES)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    provider = models.ForeignKey(
        Provider, related_name="services", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.title} {self.price}"

    class Meta:
        ordering = ['pk']
