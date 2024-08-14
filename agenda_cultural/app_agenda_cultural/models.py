from django.db import models

class Evento(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    local = models.CharField(max_length=100)
    data = models.DateTimeField()

    def __str__(self):
        return self.nome
