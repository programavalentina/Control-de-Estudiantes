from django import forms
from classrooms.models import ClassRoom, Task

class ClassRoomForm(forms.ModelForm):

	class Meta:
		model = ClassRoom
		fields = ('name', 'section', 'description')
		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control'}),
			'section': forms.TextInput(attrs={'class':'form-control'}),
			'description': forms.Textarea(attrs={'class':'form-control'}),
		}

class TaskForm(forms.ModelForm):

	class Meta:
		model = Task
		fields = ('name', 'description', 'score', 'delivery_date', 'classroom')
		widgets = {
			'classroom': forms.Select(attrs={'class':'form-control'}),
		}
