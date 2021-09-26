from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import MatriculaViewSet, Matricula_TurmaViewSet

router = DefaultRouter()
router.register('matricula', MatriculaViewSet, basename='matricula')
router.register('matricula_turma', Matricula_TurmaViewSet, basename='matricula_turma')



urlpatterns = [
    url('', include(router.urls))
]
