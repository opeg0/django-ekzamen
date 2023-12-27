from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

class Penalty(models.Model):
    penalty_type_choices = {
        'penalty1': 'предупреждение',
        'penalty2': 'административный штраф',
        'penalty3': 'лишение прав'
    }

    name = models.CharField(max_length=150)
    description = models.TextField(blank=False, null=False)
    penalty_type = models.CharField(max_length=10, choices=penalty_type_choices, default='penalty1')

    def __str__(self):
        return self.name
