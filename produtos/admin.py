from django.contrib import admin
from produtos.models import Produto

admin.site.site_header = 'Projeto CRUD'

class ListandoProdutos(admin.ModelAdmin):
    list_display = ("lm", "titulo", "preco", "link")
    list_display_links = ("lm","titulo")
    list_per_page = 20
    list_filter = ('usuario'),
    search_fields = ("lm", "titulo",)
    ordering = ('titulo',)
    

admin.site.register(Produto, ListandoProdutos)
