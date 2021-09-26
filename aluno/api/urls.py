from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import AlunoViewset, EncarregadoViewSet, EnderecoViewSet, FiliacaoViewSet, TelefoneViewSet

router = DefaultRouter()
router.register('aluno', AlunoViewset, basename='aluno')
router.register('encarregado', EncarregadoViewSet, basename='encarregado')
router.register('endereco', EnderecoViewSet, basename='endereco')
router.register('filiacao', FiliacaoViewSet, basename='filiacao')
router.register('telefone', TelefoneViewSet, basename='telefone')


urlpatterns = [
    url('', include(router.urls))
]
