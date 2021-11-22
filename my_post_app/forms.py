from django import forms
from django.core.exceptions import ValidationError

class PostForm(forms.Form):
    name = forms.CharField(max_length=100, label="Название поста", widget=forms.TextInput(attrs={
        "placeholder": "Введите название поста"
    }))
    description = forms.CharField(max_length=255, label="Описание поста", widget=forms.TextInput(attrs={
        "placeholder": "Введите описание поста"
    }))

    def clean(self):
        name = self.cleaned_data['name']
        if (len(name)>3 and len(name)<8):
            raise ValidationError('Не правильно ввели название поста')
        return self.cleaned_data