from django import forms
from models import Post


class CreatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введіть заголовок'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введіть опис'})
        }


