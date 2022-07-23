from django.urls import path
from blog.views import *

urlpatterns = [
    path('', Minha_home.as_view(), name='home'),
    path('posts/', Minha_listagem.as_view(), name='listagem'),
    path('posts/add/', CriaFormView.as_view(), name='add'),
    path('posts/<int:pk>/', Meu_detalhe.as_view(), name='detalhe'),
    path('posts/<int:pk>/edit', EditaFormView.as_view(), name='edit'),
]