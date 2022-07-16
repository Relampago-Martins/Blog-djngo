from django.urls import path
from blog.views import *

app_name = 'blog'
urlpatterns = {
    path('', Minha_home.as_view(), name='home'),
    path('posts/', Minha_listagem.as_view(), name='listagem'),
    path('posts/<int:pk>/', Meu_detalhe.as_view(), name='detalhe'),
    path('posts/cadastro/', CriaFormView.as_view(), name='formulario'),
    path('posts/edit/<int:pk>/', EditaFormView.as_view(), name='alteracao'),
}