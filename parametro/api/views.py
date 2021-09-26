from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets
from .serializers import SalaSerializer, PeriodoSerializer, ClasseSerializer, TurmaSerializer
from parametro.models import Sala, Periodo, Classe, Turma
import json
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
import os



class SalaViewSet(viewsets.ModelViewSet):
    serializer_class = SalaSerializer
    #throttle_scope = "aluno_app"
    
    def get_queryset(self):
        salas = Sala.objects.all()
        return salas

    def destroy(self, request, *args, **kwargs):
        logedin_user = request.user
        if(logedin_user == "admin"):
            sala = self.get_object()
            sala.delete()
            response_message = {"message": "A Sala foi removida com sucesso!"}
        else:
            response_message = {"message": "Não tens permissão para executar essa acção"}

        return Response(response_message)


class PeriodoViewSet(viewsets.ModelViewSet):
    serializer_class = PeriodoSerializer
    #throttle_scope = "aluno_app"
    
    def get_queryset(self):
        periodos = Periodo.objects.all()
        return periodos

    def destroy(self, request, *args, **kwargs):
        logedin_user = request.user
        if(logedin_user == "admin"):
            periodo = self.get_object()
            periodo.delete()
            response_message = {"message": "O Periodo foi removido com sucesso!"}
        else:
            response_message = {"message": "Não tens permissão para executar essa acção"}

        return Response(response_message)


class ClasseViewSet(viewsets.ModelViewSet):
    serializer_class = ClasseSerializer
    #throttle_scope = "aluno_app"
    
    def get_queryset(self):
        classes = Classe.objects.all()
        return classes

    def destroy(self, request, *args, **kwargs):
        logedin_user = request.user
        if(logedin_user == "admin"):
            classe = self.get_object()
            classe.delete()
            response_message = {"message": "A Classe foi removida com sucesso!"}
        else:
            response_message = {"message": "Não tens permissão para executar essa acção"}

        return Response(response_message)


class TurmaViewSet(viewsets.ModelViewSet):
    serializer_class = TurmaSerializer
    #throttle_scope = "aluno_app"
    
    def get_queryset(self):
        turmas = Turma.objects.all()
        return turmas

    def destroy(self, request, *args, **kwargs):
        logedin_user = request.user
        if(logedin_user == "admin"):
            turma = self.get_object()
            turma.delete()
            response_message = {"message": "A Turma foi removida com sucesso!"}
        else:
            response_message = {"message": "Não tens permissão para executar essa acção"}

        return Response(response_message)

