from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Book(models.Model):
    isbn = models.CharField(max_length=13, unique=True)
    title = models.CharField(max_length=128)
    publisher = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    pages = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('books:detail', kwargs={'isbn': self.isbn})
