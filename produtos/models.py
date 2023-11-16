from django.db import models
from datetime import datetime

class Produto(models.Model):
    lm = models.CharField(max_length=20, primary_key=True, null=False, blank=False)
    titulo = models.CharField(max_length=100, null=False, blank=False)
    preco = models.FloatField(max_length=10, null=False, blank=False)
    link = models.CharField(max_length=200, null=False, blank=False)
    avaliacoes = models.IntegerField(max_length=4, null=False, blank=False)
    media_avaliacoes = models.FloatField(max_length=4, null=False, blank=False)
    data_produto = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return f"{self.lm}]"