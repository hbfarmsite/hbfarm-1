from django.contrib import admin
from granja.models import Ovo,  Pintinho, Raca


class OvoAdmin(admin.ModelAdmin):
    list_display = ('codigo','status', 'chocadeira',
                    'data_chocadeira', 'dias_chocadeira')
    list_filter = ('status', 'chocadeira', 'data_cadastro')
    search_fields = ['codigo']
    ordering = ['data_cadastro']
    exclude = ['data_cadastro']


class PintinhoAdmin(admin.ModelAdmin):
    list_display = ('ovo', 'codigo', 'raca', 'deficiencia', 'data_eclosao')
    list_filter = ('raca', 'deficiencia', 'data_eclosao')
    search_fields = ['raca', 'data_eclosao']
    ordering = ['data_eclosao']


class RacaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nome_cientifico')
    list_filter = ('nome', 'nome_cientifico')
    search_fields = ['nome', 'nome_cientifico']
    ordering = ['nome']


admin.site.register(Ovo, OvoAdmin)
admin.site.register(Pintinho, PintinhoAdmin)
admin.site.register(Raca, RacaAdmin)
