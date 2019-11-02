from django.urls import path
from . import views

urlpatterns = [
	path('index/', views.ClassRoomList.as_view(), name='classrooms'),
	path('create/', views.ClassRoomCreate.as_view(), name='classroomcreate'),
	path('update/<int:pk>/', views.ClassRoomUpdate.as_view(), name='classroomupdate'),
    path('delete/<int:pk>/', views.ClassRoomDelete.as_view(), name='classroomdelete'),
    path('api/', views.ClassRoomApi.as_view()),
    path('task/index/', views.TaskList.as_view(), name='tasks'),
	path('task/create/', views.TaskCreate.as_view(), name='taskcreate'),
	path('task/update/<int:pk>/', views.TaskUpdate.as_view(), name='taskupdate'),
    path('task/delete/<int:pk>/', views.TaskDelete.as_view(), name='taskdelete'),
    path('task/api/', views.TaskApi.as_view()),
]
