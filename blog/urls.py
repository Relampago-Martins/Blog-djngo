from django.urls import path
from blog.views import *

urlpatterns = {
    path('', Minha_home.as_view(), name='home'),
}