from django.db import models

class Tarefa(models.Model):
    tarefa = models.CharField('Tarefa', max_length=100)

    def __str__(self):
        return self.tarefa