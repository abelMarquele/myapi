from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets
from .serializers import MatriculaSerializer, Matricula_TurmaSerializer
from matricula.models import Matricula, Matricula_Turma
from aluno.models import Aluno 
from parametro.models import Classe, Turma
import json
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
import os



class MatriculaViewSet(viewsets.ModelViewSet):
    serializer_class = MatriculaSerializer
    #throttle_scope = "aluno_app"
    
    def get_queryset(self):
        matriculas = Matricula.objects.all()
        return matriculas
    
    def destroy(self, request, *args, **kwargs):
        logedin_user = request.user
        if(logedin_user == "admin"):
            matricula = self.get_object()
            matricula.delete()
            response_message = {"message": "A Matrícula foi removida com sucesso!"}
        else:
            response_message = {"message": "Não tens permissão para executar essa acção"}

        return Response(response_message)

    def create(self, request, *args, **kwargs):
        matricula_data = request.data

        new_matricula = Matricula.objects.create(
                    aluno=Aluno.objects.get(id=matricula_data["aluno"]), 
                    classe=Classe.objects.get(id=matricula_data["classe"]), 
                    numero_processo=matricula_data["numero_processo"], 
                    ano_lectivo=matricula_data["ano_lectivo"], 
                    conferido=matricula_data["conferido"])

        new_matricula.save()

        serializer = MatriculaSerializer(new_matricula)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        matricula_data = self.get_object()
        data = request.data

        aluno = Aluno.objects.get(id=data["aluno"])
        classe = Classe.objects.get(id=data["classe"])

        matricula_data.aluno = aluno
        matricula_data.classe = classe
        matricula_data.namePai = data["namePai"]
        matricula_data.nameMae = data["nameMae"]
        matricula_data.localTrabalhoPai = data["localTrabalhoPai"]

        matricula_data.save()

        serializer = MatriculaSerializer(matricula_data)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        matricula_object = self.get_object()
        data = request.data

        try:
            aluno = Aluno.objects.get(id=data["aluno"])
            classe = Classe.objects.get(id=data["classe"])
            matricula_object.aluno = aluno
            matricula_object.classe = classe
        except KeyError:
            pass

        matricula_object.numero_processo = data.get("numero_processo", matricula_object.numero_processo)
        matricula_object.ano_lectivo = data.get("ano_lectivo", matricula_object.ano_lectivo)
        matricula_object.conferido = data.get("conferido", matricula_object.conferido)

        matricula_object.save()

        serializer = MatriculaSerializer(matricula_object)
        return Response(serializer.data)



class Matricula_TurmaViewSet(viewsets.ModelViewSet):
    serializer_class = Matricula_TurmaSerializer
    #throttle_scope = "aluno_app"
    
    def get_queryset(self):
        matricula_turmas = Matricula_Turma.objects.all()
        return matricula_turmas

    def destroy(self, request, *args, **kwargs):
        logedin_user = request.user
        if(logedin_user == "admin"):
            matricula_turma = self.get_object()
            matricula_turma.delete()
            response_message = {"message": "A Matrícula_Turma foi removida com sucesso!"}
        else:
            response_message = {"message": "Não tens permissão para executar essa acção"}

        return Response(response_message)

    def create(self, request, *args, **kwargs):
        matricula_turmas_data = request.data

        new_matricula_turmas = Matricula_Turma.objects.create(
                    matricula=Matricula.objects.get(id=matricula_turmas_data["matricula"]), 
                    turma=Turma.objects.get(id=matricula_turmas_data["turma"]))

        new_matricula_turmas.save()

        serializer = Matricula_TurmaSerializer(new_matricula_turmas)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        matricula_turmas_data = self.get_object()
        data = request.data

        matricula = Matricula.objects.get(id=data["matricula"])
        turma = Turma.objects.get(id=data["turma"])

        matricula_turmas_data.matricula = matricula
        matricula_turmas_data.turma = turma

        matricula_turmas_data.save()

        serializer = Matricula_TurmaSerializer(matricula_turmas_data)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        matricula_turmas_object = self.get_object()
        data = request.data

        try:
            matricula = Matricula.objects.get(id=data["matricula"])
            turma = Turma.objects.get(id=data["turma"])
            matricula_turmas_object.matricula = matricula
            matricula_turmas_object.turma = turma
        except KeyError:
            pass

        matricula_turmas_object.save()

        serializer = Matricula_TurmaSerializer(matricula_turmas_object)
        return Response(serializer.data)
