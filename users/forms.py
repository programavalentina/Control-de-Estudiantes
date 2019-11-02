from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Assistance

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'address', 'telephone', 'classroom')
        widgets = {
			'classroom': forms.Select(attrs={'class':'form-control'}),
		}

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'address', 'telephone', 'classroom')

class AssistanceForm(forms.ModelForm):

	class Meta:
		model = Assistance
		fields = ('date', 'user')
		widgets = {
			'user': forms.Select(attrs={'class':'form-control'}),
		}
