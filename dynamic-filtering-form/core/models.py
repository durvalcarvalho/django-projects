from tabnanny import verbose
from django import views
from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Journal(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='journals')
    categories = models.ManyToManyField(Category, related_name='journals')
    publish_at = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField(default=0)
    reviewed = models.BooleanField(default=False)

    def __str__(self):
        formated_date = self.publish_at.strftime('%Y-%m-%d')
        return f'{self.title} by {self.author} published at {formated_date}'