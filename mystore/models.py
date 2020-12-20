from django.db import models


# Create your models here.


class Publisher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book2(models.Model):
    title = models.CharField(max_length=50)
    pub_house = models.ForeignKey(Publisher, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ManyToManyField(Author, blank=True)

    def __str__(self):
        return self.title

