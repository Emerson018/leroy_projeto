from django.db import models

class Produto(models.Model):
    lm = models.CharField(max_length=20, null=False, blank=False)
    titulo = models.CharField(max_length=100, null=False, blank=False)
    preco = models.FloatField(max_length=10, null=False, blank=False)

    def __str__(self):
        return f"LM [lm={self.lm}]"