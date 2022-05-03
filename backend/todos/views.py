from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer

# Create your views here.
class DetailTodoAPIView(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class ListTodoAPIView(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    