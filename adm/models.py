from django.db import models

# Create your models here.
class Produtos(models.Model):
    nome = models.CharField(max_length=255) 
    descricao = models.TextField(blank=True, null=True) 
    preco = models.DecimalField(max_digits=10, decimal_places=2)  
    peso = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)  
    imagem = models.ImageField(upload_to='produtos/', blank=True, null=True) 
    status = models.BooleanField(default=True)  
    data_adicionado = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.nome


class React(models.Model):
    employee = models.CharField(max_length=30)  
    departament = models.CharField(max_length=200)  