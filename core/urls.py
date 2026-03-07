from django.contrib import admin
from django.urls import path
from certificados.views import detalhe_certificado, lista_certificados
from django.contrib.auth import logout
from django.shortcuts import redirect


def deslogar(request):
    logout(request)
    return redirect('lista_certificados')


urlpatterns = [
    path('sair/', deslogar, name='logout'),
    path('admin/', admin.site.urls),

    # Link para a sua nova tabela de gerenciamento
    path('lista/', lista_certificados, name='lista_certificados'),

    # Este é o link de validação que usa o UUID por segurança
    # Ajustamos o nome para bater exatamente com o novo campo de segurança
    path('validar/<uuid:id_seguranca>/',
         detalhe_certificado, name='detalhe_certificado'),
]
