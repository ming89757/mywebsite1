from django.contrib import admin
# Register your models here.

from bookstore import models


class BookManager(admin.ModelAdmin):
    list_display = ['id', 'title']


admin.site.register(models.Book, BookManager)
admin.site.register(models.Author)
