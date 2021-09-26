from rest_framework import serializers
from questionario.models import Pergunta, Quintil_Riqueza, Historico_Saude

class PerguntaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pergunta
        fields = '__all__'
   

class Quintil_RiquezaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quintil_Riqueza
        fields = '__all__'
        depth = 1


class Historico_SaudeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historico_Saude
        fields = '__all__'
        depth = 1
   