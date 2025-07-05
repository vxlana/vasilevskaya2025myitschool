from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    middle_name = models.CharField(max_length=30, blank=True, verbose_name='Отчество')
    city = models.CharField(max_length=100, blank=True, verbose_name='Город')
    street = models.CharField(max_length=100, blank=True, verbose_name='Улица')
    house_number = models.CharField(max_length=10, blank=True, verbose_name='Номер дома')
    apartment_number = models.CharField(max_length=10, blank=True, verbose_name='Номер квартиры')
    postal_code = models.CharField(max_length=10, blank=True, verbose_name='Индекс')

    def __str__(self):
        return self.username

