import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Book(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)


    def __str__(self):
        return self.title

    def __repr__(self):
        return f'Book(title={self.title}, author={self.author}, price={self.price}'

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"pk": self.id})
    

class Review(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name="reviews"
    )
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    message = models.CharField(
        blank=False, 
        null=False, 
        max_length=255
    )


    def __str__(self):
        return self.message

    def __repr__(self):
        return f'Review(book={self.book}, author={self.author}, message={self.message}'