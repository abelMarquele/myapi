from rest_framework import serializers
from aluno.models import Aluno, Encarregado, Endereco, Filiacao, Telefone


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'telefone', 'endereco', 'encarregado','filiacao', 
                'nameAluno', 'dtNascimento', 'sexo','estado_civil','email','doc','ndoc','dtDoc','foto']
        depth = 1


class EncarregadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Encarregado
        fields = ['id', 'telefone', 'endereco', 'nameEncarregado',
                  'localTrabalho', 'profissao', 'cargo', 'grauParentesco','email']
        depth = 1


class FiliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filiacao
        fields = ['id', 'telefone', 'endereco', 'namePai',
                  'nameMae', 'localTrabalhoPai', 'localTrabalhoMae', 'profissaoPai','profissaoMae']
        depth = 1


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'


class TelefoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telefone
        fields = '__all__'

    
    

