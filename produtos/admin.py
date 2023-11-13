from django.contrib import admin
from produtos.models import Produto

admin.site.site_header = 'Projeto CRUD'

class ListandoProdutos(admin.ModelAdmin):
    list_display = ("lm", "titulo", "preco", "link")
    list_display_links = ("lm","titulo")
    search_fields = ("lm", "titulo",)
    list_per_page = 20

admin.site.register(Produto, ListandoProdutos)