from django_filters import rest_framework as filters
from .models import Livro

class LivroFilter(filters.FilterSet):
    titulo = filters.CharFilter(lookup_expr='icontains')
    autor = filters.CharFilter(field_name='autor__nome', lookup_expr='icontains')
    categoria = filters.AllValuesFilter(field_name='categoria__nome')

    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'categoria']
from django_filters import rest_framework as filters
from .models import Autor, Categoria

class AutorFilter(filters.FilterSet):
    nome = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Autor
        fields = ['nome']

class CategoriaFilter(filters.FilterSet):
    nome = filters.CharFilter(lookup_expr='istartswith')

    class Meta:
        model = Categoria
        fields = ['nome']
