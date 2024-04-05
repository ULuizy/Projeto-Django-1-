from django.urls import path
from app_cad_produtos import views
urlpatterns = [
    #rota, view responsavel, nome de referencia
    path('',views.home, name='home' ),
    path('produtos/',views.produtos, name='listagem_produtos')
]
