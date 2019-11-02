# api rest
from rest_framework import serializers
from classrooms.models import ClassRoom, Task

class ClassRoomSerializer(serializers.ModelSerializer):
	class Meta:
		model = ClassRoom
		fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields = '__all__'
