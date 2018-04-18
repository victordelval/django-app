from django.db import models

from django.core.validators import MaxLengthValidator
from django.core.validators import MinValueValidator


class Tag(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
        blank=False,
        validators=[MaxLengthValidator(50)]
    )

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(
        max_length=100,
        unique=True,
        blank=False,
        validators=[MaxLengthValidator(100)]
    )

    description = models.TextField(
        max_length=500,
        blank=True,
        validators=[MaxLengthValidator(500)]
    )

    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(0.00)]
    )

    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return ('%(title)s (%(price)s €)' %
                {'title': self.title, 'price': self.price})
