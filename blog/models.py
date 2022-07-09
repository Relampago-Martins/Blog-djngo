from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.
class Post(models.Model):
    ##Atributos
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    text = models.TextField()
    data_criacao = models.DateTimeField(default=timezone.now)
    data_pub = models.DateTimeField(blank=True, null=True)

    ##metodos
    def __str__(self):
        return f'{self.titulo} de {self.autor}'