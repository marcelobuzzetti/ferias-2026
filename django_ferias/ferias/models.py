from django.db import models

class Ferias(models.Model):
    TIPO_CARREIRA_CHOICES = [
        ('CARREIRA', 'Carreira'),
        ('TEMPORÁRIO', 'Temporário'),
    ]

    promo_nr = models.CharField(max_length=10, verbose_name='PROMO/NR', blank=True)
    posto_graduacao = models.CharField(max_length=20, verbose_name='P/G')
    nome_guerra = models.CharField(max_length=100, verbose_name='Nome de Guerra')
    tipo_carreira = models.CharField(max_length=20, choices=TIPO_CARREIRA_CHOICES, verbose_name='Carreira')
    secao = models.CharField(max_length=100, verbose_name='Seção')
    substituto = models.CharField(max_length=100, verbose_name='Substituto', blank=True)
    habilitacao = models.CharField(max_length=10, verbose_name='Habilitação', blank=True)
    periodo_aquisitivo = models.CharField(max_length=4, verbose_name='Período Aquisitivo')
    data_inicio = models.DateField(verbose_name='Data de Início')
    data_termino = models.DateField(verbose_name='Data de Término')
    data_apresentacao = models.DateField(verbose_name='Data de Apresentação')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'ferias'
        verbose_name = 'Férias'
        verbose_name_plural = 'Férias'
        ordering = ['data_inicio']

    def __str__(self):
        return f'{self.posto_graduacao} {self.nome_guerra} - {self.data_inicio}'
