from django.core.validators import RegexValidator
from django.db import models


# Create your models here.

class Endereco(models.Model):
    provincia = models.CharField(verbose_name=('Província'),
                            max_length=30,
                            default='',
                            blank=True)
    cidade = models.CharField(verbose_name=('Cidade'),
                            max_length=30,
                            default='',
                            blank=True)
    distrito = models.CharField(verbose_name=('Distrito'),
                            max_length=30,
                            default='',
                            blank=True)
    bairro = models.CharField(verbose_name=('Bairro'),
                            max_length=30,
                            default='',
                            blank=True)
    av_rua = models.CharField(verbose_name=('Av/Rua'),
                            max_length=30,
                            default='',
                            blank=True)
    quarterao = models.CharField(verbose_name=('Nº de Quarterão'),
                            max_length=5,
                            default='',
                            blank=True)
    casa = models.CharField(verbose_name=('Nº de Casa'),
                            max_length=5,
                            default='',
                            blank=True)

    class Meta:
        ordering = ('provincia',)
    
    def __str__(self):
        return self.provincia


class Telefone(models.Model):
    tel_regex = RegexValidator(
                            regex=r'^\+?1?\d{5,15}$', 
                            message="O numero deve ter esse formato: '+999999999'")
    numero = models.CharField(validators=[tel_regex],
                            blank=True,
                            max_length=16, verbose_name='Nº telefone')  # validators should be a list

    class Meta:
        ordering = ('numero',)
    
    def __str__(self):
        return self.numero


class Encarregado(models.Model):
    nameEncarregado = models.CharField(verbose_name=('Nome do Encarregado/a'),
                            blank=True,
                            default='',
                            max_length=350)
    localTrabalho = models.CharField(verbose_name=('Local de Trabalho'),
                            max_length=50,
                            default='',
                            blank=True)
    profissao = models.CharField(verbose_name=('Profissão'),
                            max_length=50,
                            default='',
                            blank=True)
    cargo = models.CharField(verbose_name=('Cargo'),
                            max_length=50,
                            default='',
                            blank=True)
    grauParentesco = models.CharField(verbose_name=('Grau de Parentesco'),
                            max_length=50,
                            default='',
                            blank=True)
    email = models.EmailField(verbose_name=('Email do Encarregado/a'),
                            max_length=250, 
                            default='',
                            blank=True,
                            unique=True)
    
    telefone = models.ForeignKey(Telefone, related_name="encarregadoTelefone", on_delete=models.SET_NULL, null=True)
    endereco = models.ForeignKey(Endereco, related_name="encarregadoEndereco", on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ('nameEncarregado',)
    
    def __str__(self):
        return self.nameEncarregado



class Filiacao(models.Model):
    namePai = models.CharField(verbose_name=('Nome do Pai'),
                            blank=True,
                            default='',
                            max_length=350)
    nameMae = models.CharField(verbose_name=('Nome do Mãe'),
                            blank=True,
                            default='',
                            max_length=350)
    localTrabalhoPai = models.CharField(verbose_name=('Local de Trabalho do Pai'),
                            max_length=50,
                            default='',
                            blank=True)
    localTrabalhoMae = models.CharField(verbose_name=('Local de Trabalho da Mãe'),
                            max_length=50,
                            default='',
                            blank=True)
    profissaoPai = models.CharField(verbose_name=('Profissão do Pai'),
                            max_length=50,
                            default='',
                            blank=True)
    profissaoMae = models.CharField(verbose_name=('Profissão da Mãe'),
                            max_length=50,
                            default='',
                            blank=True)
    
    telefone = models.ForeignKey(Telefone, related_name="filiacaoTelefone", on_delete=models.SET_NULL, null=True)
    endereco = models.ForeignKey(Endereco, related_name="filiacaoEndereco", on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ('id',)
    
    def __str__(self):
        return self.namePai 


class Aluno(models.Model):
    nameAluno = models.CharField(verbose_name=('Nome Completo'),
                            blank=True,
                            default='',
                            max_length=350)
    dtNascimento = models.DateField(verbose_name=('Data de nascimento'),
                            blank=True,
                            null=True)
    SEXO_CHOICES =          (('M', u'Masculino'),
                            ('F', u'Feminino'))
    sexo = models.CharField(verbose_name=('Sexo'),
                            max_length=1,
                            choices=SEXO_CHOICES)
    ESTADO_CIVIL_CHOICES = (('S', u'Solteiro'),
                            ('C', u'Casado'),
                            ('D', u'Divorciado'),
                            ('V', u'Viúvo'))
    estado_civil = models.CharField(verbose_name=('Estado civil'),
                            max_length=1,
                            default='S',
                            choices=ESTADO_CIVIL_CHOICES)
    email = models.EmailField(verbose_name=('Email do Aluno/a'),
                            max_length=250,
                            default='',
                            blank=True, 
                            unique=True)
    doc = models.FileField(null=True, 
                            blank=True, 
                            upload_to='documents/',)
    ndoc = models.CharField(verbose_name=('Nº de BI/Cédula'),
                            max_length=20,
                            default='',
                            unique=True,
                            blank=True)
    dtDoc = models.DateField(verbose_name=('Data de Emissão'),
                            blank=True,
                            null=True)
    foto = models.ImageField(null=True, 
                            blank=True, 
                            upload_to='upload/',)


    telefone = models.ForeignKey(Telefone, related_name="estudanteTelefone", on_delete=models.SET_NULL, null=True)
    endereco = models.ForeignKey(Endereco, related_name="estudanteEndereco", on_delete=models.SET_NULL, null=True)
    encarregado = models.ForeignKey(Encarregado, related_name="estudanteEncarregado", on_delete=models.SET_NULL, null=True)
    filiacao = models.ForeignKey(Filiacao, related_name="estudanteFiliacao", on_delete=models.SET_NULL, null=True)


    class Meta:
        ordering = ('nameAluno',)
    
    def __str__(self):
        return self.nameAluno

    