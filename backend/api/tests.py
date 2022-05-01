from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from test_app.models import Book

# Create your tests here.
class APITests(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.book = Book.objects.create(
            title = "Some interesting book about API's",
            subtitle = 'Your APP can be cool!',
            author = 'Some smart Dude',
            isbn = '8238761863#1'
        )
        cls.another_book = Book.objects.create(
            title = "Some yeah",
            subtitle = 'Nice!!!',
            author = 'Postman',
            isbn = '636155194@1'
        )
    
    def test_api_listview(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 2)
        for book in Book.objects.all():
            self.assertContains(response, book)
        