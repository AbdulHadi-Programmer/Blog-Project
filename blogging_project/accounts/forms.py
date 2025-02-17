from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'fullname', 'email', 'bio']  # Include only existing fields in your model
        widgets = {
            'username': forms.TextInput(attrs={'class': 'username'}),
            'fullname': forms.TextInput(attrs={'class': 'fullname'}),
            'email': forms.EmailInput(attrs={'class': 'email'}),
            'bio': forms.Textarea(attrs={'class': 'bio'}),
        }
