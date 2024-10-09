from rest_framework import serializers
from. models import Livro, Autor, Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Categoria
        field= ['id', 'nome']
class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Autor
        fields= ['id', 'nome']
    
class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model=Livro
        fields= ['id', 'titulo', 'autor', 'categoria', 'publicado_em']
