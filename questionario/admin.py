from django.contrib import admin

from .models import Pergunta, Quintil_Riqueza, Historico_Saude

# Register your models here.

admin.site.register(Pergunta)
admin.site.register(Quintil_Riqueza)
admin.site.register(Historico_Saude)

