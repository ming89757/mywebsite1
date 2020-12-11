from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField('书名', max_length=100, unique=True)
    pub = models.CharField('出版社', max_length=200)
    price = models.IntegerField('图书价格')
    market_price = models.IntegerField('图书零售价')

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField('姓名', max_length=100,  unique=True, db_index=True)
    age = models.IntegerField('年龄', default=1)
    email = models.EmailField('邮箱', null=True)

    def __str__(self):
        return self.name

