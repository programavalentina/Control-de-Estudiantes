from users.models import CustomUser, Assistance
from django.urls import reverse_lazy
from django.views import generic
from users.serializers import UserSerializer, AssistanceSerializer # new api rest
from rest_framework import generics, viewsets # new api rest

from .forms import CustomUserCreationForm, AssistanceForm

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

# new
class UserList(generic.ListView):
	model = CustomUser
	template_name = 'list.html'

class UserUpdate(generic.UpdateView):
	model = CustomUser
	form_class = CustomUserCreationForm
	template_name = 'update.html'
	success_url = reverse_lazy('users')

class UserDelete(generic.DeleteView):
	model = CustomUser
	template_name = 'delete.html'
	success_url = reverse_lazy('users')

# api rest
class UserApi(generics.ListCreateAPIView):
	queryset = CustomUser.objects.all()
	serializer_class = UserSerializer

class AssistanceList(generic.ListView):
	model = Assistance
	template_name = 'assistances/index.html'

class AssistanceCreate(generic.CreateView):
	model = Assistance
	form_class = AssistanceForm
	template_name = 'assistances/form.html'
	success_url = reverse_lazy('assistances')

class AssistanceUpdate(generic.UpdateView):
	model = Assistance
	form_class = AssistanceForm
	template_name = 'assistances/form.html'
	success_url = reverse_lazy('assistances')

class AssistanceDelete(generic.DeleteView):
	model = Assistance
	template_name = 'assistances/delete.html'
	success_url = reverse_lazy('assistances')

# api rest
class AssistanceApi(generics.ListCreateAPIView):
	queryset = Assistance.objects.all()
	serializer_class = AssistanceSerializer

# new
class UserTestList(generic.ListView):
	model = CustomUser
	template_name = 'test.html'
