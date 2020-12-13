from django.db import models
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)


    def __str__(self):
        return self.title

    def __repr__(self):
        return f'Book(title={self.title}, author={self.author}, price={self.price}'

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"pk": self.pk})
    