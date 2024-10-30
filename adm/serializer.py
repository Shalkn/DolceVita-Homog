from rest_framework import serializers
from .models import *


class ReactSerializerProdutos(serializers.ModelSerializer):
    class Meta:
        model = Produtos
        fields = ['nome', 
                  'descricao', 
                  'preco', 
                  'peso', 
                  'imagem', 
                  'status', 
                  'data_adicionado',
                  ]
        
        
class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = React
        fields = ["employee", "departament"]
        
