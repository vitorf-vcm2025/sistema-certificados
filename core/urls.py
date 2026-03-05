from django.contrib import admin
from django.urls import path
# Importamos as duas funções da sua lógica: o detalhe e agora a lista
from certificados.views import detalhe_certificado, lista_certificados

urlpatterns = [
    path('admin/', admin.site.urls),

    # Link para a sua nova tabela de gerenciamento
    path('lista/', lista_certificados, name='lista_certificados'),

    # Este é o link de validação que usa o UUID por segurança
    path('validar/<uuid:certificado_id>/',
         detalhe_certificado, name='detalhe_certificado'),
]
