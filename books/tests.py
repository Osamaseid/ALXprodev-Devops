from django.test import TestCase
from .models import Book

class BookModelTest(TestCase):

    def setUp(self):
        # Create a sample book
        Book.objects.create(title="Test Book", author="Osama", published_year=2024)

    def test_book_creation(self):
        """Test if book is created correctly"""
        book = Book.objects.get(title="Test Book")
        self.assertEqual(book.author, "Osama")

    def test_book_count(self):
        """Test number of books"""
        count = Book.objects.count()
        self.assertEqual(count, 1)
