from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import PerguntaViewSet, Quintil_RiquezaViewSet, Historico_SaudeViewSet

router = DefaultRouter()
router.register('perguntas', PerguntaViewSet, basename='perguntas')
router.register('quintil_riqueza', Quintil_RiquezaViewSet, basename='quintil_riqueza')
router.register('historico_saude', Historico_SaudeViewSet, basename='historico_saude')




urlpatterns = [
    url('', include(router.urls))
]
