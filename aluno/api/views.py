from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets
from .serializers import AlunoSerializer, EnderecoSerializer, EncarregadoSerializer, FiliacaoSerializer, TelefoneSerializer
from aluno.models import Aluno, Telefone, Encarregado, Endereco, Filiacao
import json
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
import os
from django.core.mail import send_mail
import threading


class HandleNotifications(threading.Thread):

    def __init__(self, message, subject, recipient_list):
        self.message = message
        self.subject = subject
        self.recipient_list = recipient_list
        threading.Thread.__init__(self)

    def run(self):
        from_email = 'aamarquele@gmail.com'
        send_mail(self.subject, self.message,from_email,self.recipient_list, fail_silently=False)


class EnderecoViewSet(viewsets.ModelViewSet):
    serializer_class = EnderecoSerializer
    #throttle_scope = "aluno_app"
    
    def get_queryset(self):
        enderecos = Endereco.objects.all()
        return enderecos

    def destroy(self, request, *args, **kwargs):
        logedin_user = request.user
        if(logedin_user == "admin"):
            endereco = self.get_object()
            endereco.delete()
            response_message = {"message": "O Endereço foi removido com sucesso!"}
        else:
            response_message = {"message": "Não tens permissão para executar essa acção"}

        return Response(response_message)

    def create(self, request, *args, **kwargs):
        endereco_data = request.data

        new_endereco = Endereco.objects.create(
                    provincia=endereco_data["provincia"], 
                    cidade=endereco_data["cidade"], 
                    distrito=endereco_data["distrito"], 
                    bairro=endereco_data["bairro"], 
                    av_rua=endereco_data["av_rua"],
                    quarterao=endereco_data["quarterao"], 
                    casa=endereco_data["casa"])

        new_endereco.save()

        serializer = EnderecoSerializer(new_endereco)
        return Response(serializer.data)


class EncarregadoViewSet(viewsets.ModelViewSet):
    serializer_class = EncarregadoSerializer
    
    def get_queryset(self):
        encarregados = Encarregado.objects.all()
        return encarregados

    def destroy(self, request, *args, **kwargs):
        logedin_user = request.user
        if(logedin_user == "admin"):
            encarregado = self.get_object()
            encarregado.delete()
            response_message = {"message": "O Encarregado/a foi removido/a com sucesso!"}
        else:
            response_message = {"message": "Não tens permissão para executar essa acção"}

        return Response(response_message)

    def create(self, request, *args, **kwargs):
        encarregado_data = request.data

        new_encarregado = Encarregado.objects.create(
                    telefone=Telefone.objects.get(id=encarregado_data["telefone"]), 
                    endereco=Endereco.objects.get(id=encarregado_data["endereco"]),  
                    nameEncarregado=encarregado_data["nameEncarregado"], 
                    localTrabalho=encarregado_data["localTrabalho"], 
                    profissao=encarregado_data["profissao"], 
                    cargo=encarregado_data["cargo"], 
                    grauParentesco=encarregado_data["grauParentesco"],
                    email=encarregado_data["email"])

        new_encarregado.save()

        serializer = EncarregadoSerializer(new_encarregado)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        encarregado_object = self.get_object()
        data = request.data

        telefone = Telefone.objects.get(id=data["telefone"])
        endereco = Endereco.objects.get(id=data["endereco"])

        encarregado_object.telefone = telefone
        encarregado_object.endereco = endereco
        encarregado_object.nameEncarregado = data["nameEncarregado"]
        encarregado_object.localTrabalho = data["localTrabalho"]
        encarregado_object.profissao = data["profissao"]
        encarregado_object.cargo = data["cargo"]
        encarregado_object.grauParentesco = data["grauParentesco"]
        encarregado_object.email = data["email"]

        encarregado_object.save()

        serializer = EncarregadoSerializer(encarregado_object)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        encarregado_object = self.get_object()
        data = request.data

        try:
            telefone = Telefone.objects.get(id=data["telefone"])
            endereco = Endereco.objects.get(id=data["endereco"])
            encarregado_object.telefone = telefone
            encarregado_object.endereco = endereco
        except KeyError:
            pass

        encarregado_object.nameEncarregado = data.get("nameEncarregado", encarregado_object.nameEncarregado)
        encarregado_object.localTrabalho = data.get("localTrabalho", encarregado_object.localTrabalho)
        encarregado_object.profissao = data.get("profissao", encarregado_object.profissao)
        encarregado_object.cargo = data.get("cargo", encarregado_object.cargo)
        encarregado_object.grauParentesco = data.get("grauParentesco", encarregado_object.grauParentesco)
        encarregado_object.email = data.get("email", encarregado_object.email)

        encarregado_object.save()

        serializer = EncarregadoSerializer(encarregado_object)
        return Response(serializer.data)


class FiliacaoViewSet(viewsets.ModelViewSet):
    queryset = Filiacao.objects.all()
    serializer_class = FiliacaoSerializer
    #throttle_scope = "aluno_app"
    
    def get_queryset(self):
        filiacoes = Filiacao.objects.all()
        return filiacoes

    def destroy(self, request, *args, **kwargs):
        logedin_user = request.user
        if(logedin_user == "admin"):
            filiacao = self.get_object()
            filiacao.delete()
            response_message = {"message": "A Filiação foi removida com sucesso!"}
        else:
            response_message = {"message": "Não tens permissão para executar essa acção"}

        return Response(response_message)

    def create(self, request, *args, **kwargs):
        filiacao_data = request.data

        new_filiacao = Filiacao.objects.create(
                    telefone=Telefone.objects.get(id=filiacao_data["telefone"]), 
                    endereco=Endereco.objects.get(id=filiacao_data["endereco"]), 
                    namePai=filiacao_data["namePai"], 
                    nameMae=filiacao_data["nameMae"], 
                    localTrabalhoPai=filiacao_data["localTrabalhoPai"], 
                    localTrabalhoMae=filiacao_data["localTrabalhoMae"], 
                    profissaoPai=filiacao_data["profissaoPai"],
                    profissaoMae=filiacao_data["profissaoMae"])

        new_filiacao.save()

        serializer = FiliacaoSerializer(new_filiacao)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        filiacao_data = self.get_object()
        data = request.data

        telefone = Telefone.objects.get(id=data["telefone"])
        endereco = Endereco.objects.get(id=data["endereco"])

        filiacao_data.telefone = telefone
        filiacao_data.endereco = endereco
        filiacao_data.namePai = data["namePai"]
        filiacao_data.nameMae = data["nameMae"]
        filiacao_data.localTrabalhoPai = data["localTrabalhoPai"]
        filiacao_data.localTrabalhoMae = data["localTrabalhoMae"]
        filiacao_data.profissaoPai = data["profissaoPai"]
        filiacao_data.profissaoMae = data["profissaoMae"]

        filiacao_data.save()

        serializer = FiliacaoSerializer(filiacao_data)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        filiacao_object = self.get_object()
        data = request.data

        try:
            telefone = Telefone.objects.get(id=data["telefone"])
            endereco = Endereco.objects.get(id=data["endereco"])
            filiacao_object.telefone = telefone
            filiacao_object.endereco = endereco
        except KeyError:
            pass

        filiacao_object.namePai = data.get("namePai", filiacao_object.namePai)
        filiacao_object.nameMae = data.get("nameMae", filiacao_object.nameMae)
        filiacao_object.localTrabalhoPai = data.get("localTrabalhoPai", filiacao_object.localTrabalhoPai)
        filiacao_object.localTrabalhoMae = data.get("localTrabalhoMae", filiacao_object.localTrabalhoMae)
        filiacao_object.profissaoPai = data.get("profissaoPai", filiacao_object.profissaoPai)
        filiacao_object.profissaoMae = data.get("profissaoMae", filiacao_object.profissaoMae)

        filiacao_object.save()

        serializer = FiliacaoSerializer(filiacao_object)
        return Response(serializer.data)


class TelefoneViewSet(viewsets.ModelViewSet):
    serializer_class = TelefoneSerializer
    #throttle_scope = "aluno_app"
    
    def get_queryset(self):
        telefones = Telefone.objects.all()
        return telefones

    def destroy(self, request, *args, **kwargs):
        logedin_user = request.user
        if(logedin_user == "admin"):
            telefone = self.get_object()
            telefone.delete()
            response_message = {"message": "O Telefone foi removido com sucesso!"}
        else:
            response_message = {"message": "Não tens permissão para executar essa acção"}

        return Response(response_message)

    def create(self, request, *args, **kwargs):
        telefone_data = request.data

        new_telafone = Telefone.objects.create(
                    numero=telefone_data["numero"])

        new_telafone.save()

        serializer = TelefoneSerializer(new_telafone)
        return Response(serializer.data)


class AlunoViewset(viewsets.ModelViewSet):
    serializer_class = AlunoSerializer
    #throttle_scope = "aluno_app"

    def send_email(self, message, subject, recipient_list):
        from_email = 'aamarquele@gmail.com'
        send_mail(subject, message,from_email,recipient_list, fail_silently=False)
    
    def get_queryset(self):
        alunos = Aluno.objects.all()
        return alunos

    def create(self, request, *args, **kwargs):
        aluno_data = request.data

        new_aluno = Aluno.objects.create(
                    telefone=Telefone.objects.get(id=aluno_data["telefone"]), 
                    endereco=Endereco.objects.get(id=aluno_data["endereco"]), 
                    encarregado=Encarregado.objects.get(id=aluno_data["encarregado"]), 
                    filiacao=Filiacao.objects.get(id=aluno_data["filiacao"]), 
                    nameAluno=aluno_data["nameAluno"], 
                    dtNascimento=aluno_data["dtNascimento"], 
                    sexo=aluno_data["sexo"], 
                    estado_civil=aluno_data["estado_civil"], 
                    email=aluno_data["email"],
                    doc=aluno_data["doc"], 
                    ndoc=aluno_data["ndoc"], 
                    dtDoc=aluno_data["dtDoc"], 
                    foto=aluno_data["foto"])

        new_aluno.save()
        HandleNotifications("O aluno foi registado no sistema", "Notificação",['aamarquele@gmail.com',]).start()
        serializer = AlunoSerializer(new_aluno)

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        logedin_user = request.user
        if(logedin_user == "admin"):
            aluno = self.get_object()
            aluno.delete()
            response_message = {"message": "O aluno/a foi removido/a com sucesso!"}
        else:
            response_message = {"message": "Não tens permissão para executar essa acção"}

        return Response(response_message)

    def update(self, request, *args, **kwargs):
        aluno_object = self.get_object()
        data = request.data

        telefone = Telefone.objects.get(id=data["telefone"])
        endereco = Endereco.objects.get(id=data["endereco"])
        encarregado = Encarregado.objects.get(id=data["encarregado"])
        filiacao = Filiacao.objects.get(id=data["filiacao"])

        aluno_object.telefone = telefone
        aluno_object.endereco = endereco
        aluno_object.encarregado = encarregado
        aluno_object.filiacao = filiacao
        aluno_object.nameAluno = data["nameAluno"]
        aluno_object.dtNascimento = data["dtNascimento"]
        aluno_object.sexo = data["sexo"]
        aluno_object.estado_civil = data["estado_civil"]
        aluno_object.email = data["email"]
        aluno_object.doc = data["doc"]
        aluno_object.ndoc = data["ndoc"]
        aluno_object.dtDoc = data["dtDoc"]
        aluno_object.foto = data["foto"]

        aluno_object.save()

        serializer = AlunoSerializer(aluno_object)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        aluno_object = self.get_object()
        data = request.data

        try:
            telefone = Telefone.objects.get(id=data["telefone"])
            endereco = Endereco.objects.get(id=data["endereco"])
            encarregado = Encarregado.objects.get(id=data["encarregado"])
            filiacao = Filiacao.objects.get(id=data["filiacao"])
            aluno_object.telefone = telefone
            aluno_object.endereco = endereco
            aluno_object.encarregado = encarregado
            aluno_object.filiacao = filiacao
        except KeyError:
            pass

        aluno_object.nameAluno = data.get("nameAluno", aluno_object.nameAluno)
        aluno_object.dtNascimento = data.get("dtNascimento", aluno_object.dtNascimento)
        aluno_object.sexo = data.get("sexo", aluno_object.sexo)
        aluno_object.estado_civil = data.get("estado_civil", aluno_object.estado_civil)
        aluno_object.email = data.get("email", aluno_object.email)
        aluno_object.doc = data.get("doc", aluno_object.doc)
        aluno_object.ndoc = data.get("ndoc", aluno_object.ndoc)
        aluno_object.dtDoc = data.get("dtDoc", aluno_object.dtDoc)
        aluno_object.foto = data.get("foto", aluno_object.foto)

        aluno_object.save()

        serializer = AlunoSerializer(aluno_object)
        return Response(serializer.data)

