from classrooms.models import ClassRoom, Task
from django.urls import reverse_lazy
from django.views import generic
from classrooms.serializers import ClassRoomSerializer, TaskSerializer # new api rest
from rest_framework import generics, viewsets # new api rest

from .forms import ClassRoomForm, TaskForm

class ClassRoomList(generic.ListView):
	model = ClassRoom
	template_name = 'classrooms/index.html'

class ClassRoomCreate(generic.CreateView):
	model = ClassRoom
	form_class = ClassRoomForm
	template_name = 'classrooms/form.html'
	success_url = reverse_lazy('classrooms')

class ClassRoomUpdate(generic.UpdateView):
	model = ClassRoom
	form_class = ClassRoomForm
	template_name = 'classrooms/form.html'
	success_url = reverse_lazy('classrooms')

class ClassRoomDelete(generic.DeleteView):
	model = ClassRoom
	template_name = 'classrooms/delete.html'
	success_url = reverse_lazy('classrooms')

# api rest
class ClassRoomApi(generics.ListCreateAPIView):
	queryset = ClassRoom.objects.all()
	serializer_class = ClassRoomSerializer

class TaskList(generic.ListView):
	model = Task
	template_name = 'tasks/index.html'

class TaskCreate(generic.CreateView):
	model = Task
	form_class = TaskForm
	template_name = 'tasks/form.html'
	success_url = reverse_lazy('tasks')

class TaskUpdate(generic.UpdateView):
	model = Task
	form_class = TaskForm
	template_name = 'tasks/form.html'
	success_url = reverse_lazy('tasks')

class TaskDelete(generic.DeleteView):
	model = Task
	template_name = 'tasks/delete.html'
	success_url = reverse_lazy('tasks')

# api rest
class TaskApi(generics.ListCreateAPIView):
	queryset = Task.objects.all()
	serializer_class = TaskSerializer
