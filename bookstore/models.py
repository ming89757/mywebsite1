from django.db import models


# Create your models here.


class Book(models.Model):
    title = models.CharField('书名', max_length=100)
    pub = models.CharField('出版社', max_length=200, null=True)
    price = models.DecimalField('价格',
                                max_digits=12,
                                decimal_places=2,
                                default=0)
    market_price = models.DecimalField('零售价',
                                       max_digits=12,
                                       decimal_places=2,
                                       default=9999)

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField('姓名', max_length=100, blank=False, unique=True, db_index=True)
    age = models.IntegerField('年龄', null=False, default=1)
    email = models.EmailField('邮箱', null=True)

    def __str__(self):
        return self.name
