from django.contrib import admin

from .models import Aluno, Encarregado, Endereco, Filiacao, Telefone

# Register your models here.

admin.site.register(Aluno)
admin.site.register(Encarregado)
admin.site.register(Endereco)
admin.site.register(Filiacao)
admin.site.register(Telefone)

