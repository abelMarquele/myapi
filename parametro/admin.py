from django.contrib import admin

from .models import Disciplina, Sala, Periodo, Classe, Turma

# Register your models here.

admin.site.register(Sala)
admin.site.register(Periodo)
admin.site.register(Classe)
admin.site.register(Disciplina)
admin.site.register(Turma)

