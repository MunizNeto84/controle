from django.contrib import admin
from controle.models import Receita, Despesa

class Receitas(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'valor', 'data')
    list_display_links = ('id',)
    search_fields = ('descricao',)
    list_per_page = 20

admin.site.register(Receita, Receitas)

class Depesas(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'valor', 'data')
    list_display_links = ('id',)
    search_fields = ('descricao',)
    list_per_page = 20

admin.site.register(Despesa, Depesas)

