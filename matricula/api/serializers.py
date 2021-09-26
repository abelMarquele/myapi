from rest_framework import serializers
from matricula.models import Matricula, Matricula_Turma

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'
        depth = 1
   


class Matricula_TurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula_Turma
        fields = '__all__'
        depth = 1
   

