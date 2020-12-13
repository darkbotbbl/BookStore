from django.test import TestCase
from .models import Book
from django.urls import reverse, resolve
from .views import BookListView


class BookTests(TestCase):

    def setUp(self):
        url = reverse("book_list")
        self.response = self.client.get(url)

    def test_book_object_creation(self):
        book = Book.objects.create(
            title="The first book",
            author="Malor Kaduna",
            price=520.22,
        )
        self.assertEqual(book.title, "The first book")
        self.assertEqual(book.author, "Malor Kaduna")
        self.assertEqual(book.price, 520.22)

    # TODO - add tests for the urls, templates, and views 
    def test_books_list_template(self):
        self.assertTemplateUsed(self.response, "books/book_list.html")
        self.assertContains(self.response, "Books")
        self.assertNotContains(self.response, "These are books")

    def test_book_list_view(self):
        view = resolve("/books/")
        self.assertEqual(
            view.func.__name__,
            BookListView.as_view().__name__
        )