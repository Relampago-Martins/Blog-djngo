from tkinter import Widget
from django.forms import *
from blog.models import *

class MeuForm(ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'text', 'data_pub']
        labels = {
            'titulo': 'Título',
            'text' : 'Corpo do post',
            'data_pub' : 'Data de publicação',
        }
        widgets = {
            'titulo' :  TextInput(attrs={'class':'form-control'}),
            'text' :  Textarea(attrs={'class':'form-control'}),
            'data_pub' :   DateTimeInput(attrs={'class':'form-control'}),
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        labels = {
            'comment' : 'Comente aqui',
        }
        widgets = {
            'comment' :  TextInput(attrs={
                'class':'form-control',
                'placeholder': 'Digite seu comentário',
                }),
        }
