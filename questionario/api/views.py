from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets
from .serializers import PerguntaSerializer, Quintil_RiquezaSerializer, Historico_SaudeSerializer
from questionario.models import Pergunta, Quintil_Riqueza, Historico_Saude
import json
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
import os



class PerguntaViewSet(viewsets.ModelViewSet):
    serializer_class = PerguntaSerializer
    #throttle_scope = "aluno_app"
    
    def get_queryset(self):
        perguntas = Pergunta.objects.all()
        return perguntas

    def destroy(self, request, *args, **kwargs):
        logedin_user = request.user
        if(logedin_user == "admin"):
            pergunta = self.get_object()
            pergunta.delete()
            response_message = {"message": "A Pergunta foi removida com sucesso!"}
        else:
            response_message = {"message": "Não tens permissão para executar essa acção"}

        return Response(response_message)


class Quintil_RiquezaViewSet(viewsets.ModelViewSet):
    serializer_class = Quintil_RiquezaSerializer
    #throttle_scope = "aluno_app"
    
    def get_queryset(self):
        quintil_riqueza = Quintil_Riqueza.objects.all()
        return quintil_riqueza

    def destroy(self, request, *args, **kwargs):
        logedin_user = request.user
        if(logedin_user == "admin"):
            quintil_riqueza = self.get_object()
            quintil_riqueza.delete()
            response_message = {"message": "O Quintil de Riqueza foi removido com sucesso!"}
        else:
            response_message = {"message": "Não tens permissão para executar essa acção"}

        return Response(response_message)

    def create(self, request, *args, **kwargs):
        quintil_riqueza_data = request.data

        new_quintil_riqueza = Quintil_Riqueza.objects.create(
                    pergunta=Pergunta.objects.get(id=quintil_riqueza_data["pergunta"]), 
                    resposta=quintil_riqueza_data["resposta"])

        new_quintil_riqueza.save()

        serializer = Quintil_RiquezaSerializer(new_quintil_riqueza)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        quintil_riqueza_data = self.get_object()
        data = request.data

        pergunta = Pergunta.objects.get(id=data["pergunta"])
        quintil_riqueza_data.pergunta = pergunta
        quintil_riqueza_data.resposta = data["resposta"]

        quintil_riqueza_data.save()

        serializer = Quintil_RiquezaSerializer(quintil_riqueza_data)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        quintil_riqueza_object = self.get_object()
        data = request.data

        try:
            pergunta = Pergunta.objects.get(id=data["pergunta"])
            quintil_riqueza_object.pergunta = pergunta
        except KeyError:
            pass

        quintil_riqueza_object.resposta = data.get("resposta", quintil_riqueza_object.resposta)

        quintil_riqueza_object.save()

        serializer = Quintil_RiquezaSerializer(quintil_riqueza_object)
        return Response(serializer.data)



class Historico_SaudeViewSet(viewsets.ModelViewSet):
    serializer_class = Historico_SaudeSerializer
    #throttle_scope = "aluno_app"
    
    def get_queryset(self):
        historico_saude = Historico_Saude.objects.all()
        return historico_saude

    def destroy(self, request, *args, **kwargs):
        logedin_user = request.user
        if(logedin_user == "admin"):
            historico_saude = self.get_object()
            historico_saude.delete()
            response_message = {"message": "O Historico de Saúde foi removido com sucesso!"}
        else:
            response_message = {"message": "Não tens permissão para executar essa acção"}

        return Response(response_message)

    def create(self, request, *args, **kwargs):
        historico_saude_data = request.data

        new_historico_saude = Historico_Saude.objects.create(
                    pergunta=Pergunta.objects.get(id=historico_saude_data["pergunta"]), 
                    resposta=historico_saude_data["resposta"])

        new_historico_saude.save()

        serializer = Historico_SaudeSerializer(new_historico_saude)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        historico_saude_data = self.get_object()
        data = request.data

        pergunta = Pergunta.objects.get(id=data["pergunta"])
        historico_saude_data.pergunta = pergunta
        historico_saude_data.resposta = data["resposta"]

        historico_saude_data.save()

        serializer = Historico_SaudeSerializer(historico_saude_data)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        historico_saude_object = self.get_object()
        data = request.data

        try:
            pergunta = Pergunta.objects.get(id=data["pergunta"])
            historico_saude_object.pergunta = pergunta
        except KeyError:
            pass

        historico_saude_object.resposta = data.get("resposta", historico_saude_object.resposta)

        historico_saude_object.save()

        serializer = Historico_SaudeSerializer(historico_saude_object)
        return Response(serializer.data)


