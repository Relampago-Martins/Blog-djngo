from django.shortcuts import render
from django.views import generic
# Create your views here.

class Minha_home(generic.TemplateView):
    template_name = "blog/posts.html"