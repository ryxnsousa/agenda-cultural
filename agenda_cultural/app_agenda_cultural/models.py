from django.db import models
import datetime

class Evento(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    local = models.CharField(max_length=100)
    data = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.nome