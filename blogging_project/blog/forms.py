from django import forms
from .models import Post, Profile


from django import forms
from .models import Post, Profile


class PostForm(forms.ModelForm):
    class Meta:
        model = Post 
        fields = ['title', 'content', 'author', 'category', 'tags', 'views']
        widgets = {
            "title": forms.TextInput(attrs={'class': 'title'}),
            "content": forms.Textarea(attrs={'class': 'content'}),  # Fixed "Textarea"
            "author": forms.Select(attrs={'class': 'author'}),
            "category": forms.TextInput(attrs={'class': 'category'}),
            "tags": forms.TextInput(attrs={'class': 'tags'}),
            "views": forms.TextInput(attrs={'class': 'views'}),
        }



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture']
        widgets = {
            'bio': forms.TextInput(attrs={'class': 'bio'}),
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'picture'}),
        }



