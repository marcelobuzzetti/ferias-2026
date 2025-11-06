from django.contrib import admin
from .models import Ferias


@admin.register(Ferias)
class FeriasAdmin(admin.ModelAdmin):
    list_display = ['posto_graduacao', 'nome_guerra', 'data_inicio', 'data_termino', 'data_apresentacao', 'secao']
    list_filter = ['tipo_carreira', 'secao', 'data_inicio', 'data_termino']
    search_fields = ['nome_guerra', 'posto_graduacao', 'promo_nr', 'secao']
    date_hierarchy = 'data_inicio'
    ordering = ['-data_inicio']
    
    fieldsets = (
        ('Identificação', {
            'fields': ('promo_nr', 'posto_graduacao', 'nome_guerra', 'tipo_carreira')
        }),
        ('Lotação', {
            'fields': ('secao', 'substituto', 'habilitacao')
        }),
        ('Período de Férias', {
            'fields': ('periodo_aquisitivo', 'data_inicio', 'data_termino', 'data_apresentacao')
        }),
    )

