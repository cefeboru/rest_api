from rest_framework import generics
from .models import listItem
from .serializers import TaskSerializer


class TasksList(generics.ListCreateAPIView):
	"""
	List all tasks, or create a new task.
	"""
	queryset = listItem.objects.all()
	serializer_class = TaskSerializer

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
	"""
	Retrieve, update or delete a Task.
	"""
	queryset = listItem.objects.all()
	serializer_class = TaskSerializer