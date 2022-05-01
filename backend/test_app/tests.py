from django.test import TestCase
from django.urls import reverse
from .models import Book

# Create your tests here.
class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.book = Book.objects.create(
            title='Nice Book',
            subtitle='Some nice Subtitle',
            author='Some nice Author',
            isbn='12321371541',
        )
    def test_book_content(self) -> None:
        self.assertEqual(self.book.title, 'Nice Book')
        self.assertEqual(self.book.subtitle, 'Some nice Subtitle') 
        self.assertEqual(self.book.author, 'Some nice Author') 
        self.assertEqual(self.book.isbn, '12321371541')

    def test_book_listview(self) -> None:
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Some nice Subtitle')
        self.assertTemplateUsed(response, 'books/book_list.html')