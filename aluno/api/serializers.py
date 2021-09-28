from django.db.models import fields
from rest_framework import serializers
from aluno.models import Aluno, Encarregado, Endereco, Filiacao, Telefone


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id','nameAluno', 'dtNascimento', 'sexo','estado_civil','email','doc','ndoc','dtDoc','foto'
                    ,'endereco', 'encarregado','filiacao' ,'telefone' ]
        depth = 1


class EncarregadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Encarregado
        fields = ['id', 'nameEncarregado','localTrabalho', 'profissao', 'cargo', 'grauParentesco','email'
                    , 'telefone', 'endereco']
        depth = 1


class FiliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filiacao
        fields = ['id','namePai','nameMae', 'localTrabalhoPai', 'localTrabalhoMae', 'profissaoPai','profissaoMae', 
                    'telefone', 'endereco']
        depth = 1


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'


class TelefoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telefone
        fields = '__all__'

    
    

