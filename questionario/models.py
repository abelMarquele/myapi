from django.db import models

# Create your models here.

class Pergunta(models.Model):
    codigoPergunta  = models.CharField(verbose_name=('código da Pergunta'),
                            max_length=30,
                            default='',
                            blank=True)
    pergunta = models.CharField(verbose_name=('Pergunta'),
                            max_length=500,
                            default='',
                            blank=True)

    class Meta:
        ordering = ('codigoPergunta',)
    
    def __str__(self):
        return self.codigoPergunta


class Quintil_Riqueza(models.Model):
    pergunta = models.ForeignKey(Pergunta, related_name="riquezaPergunta", on_delete=models.CASCADE, null=True)
    resposta = models.CharField(verbose_name=('Resposta'),
                            max_length=10,
                            default='',
                            blank=True)
    def __str__(self):
        return self.pergunta


class Historico_Saude(models.Model):
    pergunta = models.ForeignKey(Pergunta, related_name="saudePergunta", on_delete=models.CASCADE, null=True)
    resposta = models.CharField(verbose_name=('Resposta'),
                            max_length=10,
                            default='',
                            blank=True)

    def __str__(self):
        return self.pergunta