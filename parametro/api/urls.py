from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import DisciplinaViewSet, SalaViewSet, PeriodoViewSet, ClasseViewSet, TurmaViewSet

router = DefaultRouter()
router.register('sala', SalaViewSet, basename='sala')
router.register('periodo', PeriodoViewSet, basename='periodo')
router.register('disciplina', DisciplinaViewSet, basename='disciplina')
router.register('classe', ClasseViewSet, basename='classe')
router.register('turma', TurmaViewSet, basename='turma')



urlpatterns = [
    url('', include(router.urls))
]
