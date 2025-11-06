from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_ferias, name='listar_ferias'),
    path('criar/', views.criar_ferias, name='criar_ferias'),
    path('editar/<int:pk>/', views.editar_ferias, name='editar_ferias'),
    path('deletar/<int:pk>/', views.deletar_ferias, name='deletar_ferias'),
    path('visualizar/<int:pk>/', views.visualizar_ferias, name='visualizar_ferias'),
]
