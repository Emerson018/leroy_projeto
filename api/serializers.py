from rest_framework import serializers
from produtos.models import Produto

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ('lm', 'titulo', 'preco', 'media_avaliacoes', 'link', \
                  'avaliacoes','data_produto', 'foto')