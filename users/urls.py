from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('all/', views.UserList.as_view(), name='users'),
    path('update/<int:pk>/', views.UserUpdate.as_view(), name='userupdate'),
    path('delete/<int:pk>/', views.UserDelete.as_view(), name='userdelete'),
    path('api/', views.UserApi.as_view()),
    path('assistance/create', views.AssistanceCreate.as_view(), name='assistancecreate'),
    path('assistance/index', views.AssistanceList.as_view(), name='assistances'),
    path('assistace/update/<int:pk>/', views.AssistanceUpdate.as_view(), name='assistanceupdate'),
    path('assistace/delete/<int:pk>/', views.AssistanceDelete.as_view(), name='assistancedelete'),
    path('assistance/api/', views.AssistanceApi.as_view()),
    path('table/', views.UserTestList.as_view(), name='test'),
]
