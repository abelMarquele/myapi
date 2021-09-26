from django.db import models

# Create your models here.

class Sala(models.Model):
    nameSala = models.CharField(verbose_name=('Nome da Sala'),
                            blank=True,
                            default='',
                            max_length=100)
    capacidade = models.CharField(verbose_name=('Capacidade'),
                            max_length=50,
                            default='',
                            blank=True)
    tipoSala = models.CharField(verbose_name=('Tipo de Sala'),
                            max_length=50,
                            default='',
                            blank=True)

    class Meta:
        ordering = ('nameSala',)
    
    def __str__(self):
        return self.nameSala

class Periodo(models.Model):
    hora_inicio = models.DateTimeField(verbose_name=('Hora de início'),
                            blank=True,
                            null=True)
    hora_fim = models.DateTimeField(verbose_name=('Hora do fim'),
                            max_length=50,
                            default='',
                            blank=True)
    periodo = models.CharField(verbose_name=('Periodo'),
                            max_length=50,
                            default='',
                            blank=True)
    turno = models.CharField(verbose_name=('Turno'),
                            max_length=50,
                            default='',
                            blank=True)

    class Meta:
        ordering = ('periodo',)
    
    def __str__(self):
        return self.periodo


class Classe(models.Model):
    nomeClasse = models.CharField(verbose_name=('Nome da Sala'),
                            max_length=50,
                            default='',
                            blank=True)

    class Meta:
        ordering = ('nomeClasse',)
    
    def __str__(self):
        return self.nomeClasse


class Turma(models.Model):
    nameTurma = models.CharField(verbose_name=('Nome da Turma'),
                            blank=True,
                            default='',
                            max_length=50)
    
    sala = models.ForeignKey(Sala, related_name="turmaSala", on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, related_name="turmaPeriodo", on_delete=models.CASCADE)

    class Meta:
        ordering = ('nameTurma',)
    
    def __str__(self):
        return self.nameTurma