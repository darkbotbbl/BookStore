from django.test import TestCase
from .models import Book


class BookModelTests(TestCase):

    def test_book_object_creation(self):
        book = Book.objects.create(
            title="The first book",
            author="Malor Kaduna",
            price=520.22,
        )
        self.assertEqual(book.title, "The first book")
        self.assertEqual(book.author, "Malor Kaduna")
        self.assertEqual(book.price, 520.22)