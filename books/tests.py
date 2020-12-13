from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import resolve, reverse

from .models import Book, Review
from .views import BookDetailView, BookListView


class BookTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="kweku",
            email="kweku@gmail.com",
            password="testpass1234",
        )
        self.book = Book.objects.create(
            title="The first book",
            author="Malor Kaduna",
            price=520.22,
        )
        self.review = Review.objects.create(
            author=self.user,
            book=self.book,
            message="This is a great first book"
        )

    def test_book_object_creation(self):
        self.assertEqual(self.book.title, "The first book")
        self.assertEqual(self.book.author, "Malor Kaduna")
        self.assertEqual(self.book.price, 520.22)

    def test_books_list_view(self):
        view = resolve("/books/")
        response = self.client.get(reverse("book_list"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "books/book_list.html")
        self.assertContains(response, "Books")
        self.assertNotContains(response, "These are books")
        self.assertEqual(
            view.func.__name__,
            BookListView.as_view().__name__
        )

    def test_book_detail_view(self):
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get("/books/12345")
        view = resolve(self.book.get_absolute_url())

        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertTemplateUsed(response, "books/book_detail.html")
        self.assertContains(response, "The first book")
        self.assertContains(response, "This is a great first book")
        self.assertContains(response, "kweku")
        self.assertNotContains(response, "This is awesome")
        self.assertEqual(
            view.func.__name__,
            BookDetailView.as_view().__name__
        )
