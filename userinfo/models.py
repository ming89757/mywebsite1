from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    role = models.IntegerField('role', default=1)

    def __str__(self):
        return self.name

