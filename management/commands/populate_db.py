from django.core.management.base import BaseCommand
from core.models import Categoria, Autor, Livro

class Command(BaseCommand):
    help = "Cria registros de exemplo no banco de dados"

    def handle(self, *args, **options):
        # Criar Categorias
        categoria_misterio = Categoria.objects.create(nome="Mistério")
        categoria_ficcao = Categoria.objects.create(nome="Ficção")
        # (restante do código para criação dos autores e livros conforme a especificação)
