from django.db import models

class Receita(models.Model):
    descricao = models.CharField(max_length=50)
    valor = models.FloatField()
    data = models.DateField()

    def __str__(self):
        return self.descricao

class Despesa(models.Model):
    descricao = models.CharField(max_length=50)
    valor = models.FloatField()
    data = models.DateField()

    def __str__(self):
        return self.descricao