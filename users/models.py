from django.contrib.auth.models import AbstractUser
from django.db import models
from classrooms.models import ClassRoom

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    telephone = models.IntegerField(null=True, blank=True)
    classroom = models.ForeignKey(ClassRoom, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.username

class Assistance(models.Model):
	date = models.DateField()
	user = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)
