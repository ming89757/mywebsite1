from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField('book_name', max_length=100)
    pub = models.CharField('pub', max_length=200, null=True)
