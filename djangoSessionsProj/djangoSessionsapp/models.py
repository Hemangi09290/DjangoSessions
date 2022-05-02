from django.db import models

# Create your models here.
class Author(models.Model):
    num_books = models.PositiveIntegerField()
    num_authors = models.PositiveIntegerField()
    num_visits = models.PositiveIntegerField()
