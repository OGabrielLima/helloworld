from django.urls import path
from . import views
"""todas as urls referente a gestãoacademica deverão estar nesse aquivo"""
urlpatterns = [
    path('', views.listaDespesas, name='lista-mostrardespesas'),
    path('fazerPagamento/<int:id>', views.fazerPagamento, name="alterarstatusdespesa"),
    path('tornarPendente/<int:id>', views.tornarPendente, name="tonarpendente"),
]

"""
urlpatterns = [
    path('', views.listaMatriculas, name='lista-disciplinamatricula'),
    path('fazerMatricula/<int:id>', views.fazerMatricula, name="alterarstatusmatricula"),
]
"""