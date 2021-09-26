from django.contrib import admin

from .models import Sala, Periodo, Classe, Turma

# Register your models here.

admin.site.register(Sala)
admin.site.register(Periodo)
admin.site.register(Classe)
admin.site.register(Turma)

