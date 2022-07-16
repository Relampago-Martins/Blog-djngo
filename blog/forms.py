from tkinter import Widget
from django.forms import ModelForm

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
        