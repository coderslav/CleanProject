from django.test import TestCase
from django.urls import reverse
from .models import Todo
from rest_framework import status

# Create your tests here.
class TodoTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.Todo = Todo.objects.create(
            title = 'Todo for test',
            body = 'Testing test'
        )
        cls.Todo_second = Todo.objects.create(
            title = 'Second Todo for test',
            body = 'Testing second Todo'
        )

    def test_todo_content(self):
        self.assertEqual(self.Todo.title, 'Todo for test')
        self.assertEqual(self.Todo.body, 'Testing test')
        self.assertEqual(str(self.Todo), 'Todo for test')

    def test_todoAPI_listview(self):
        response = self.client.get(reverse('todo_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 2)
        for todo in Todo.objects.all():
            self.assertContains(response, todo)
    
    def test_todoAPI_detail(self):
        response = self.client.get(reverse('todo_detail', kwargs={'pk': self.Todo_second.id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 2) 
        self.assertContains(response, 'Todo for test')
