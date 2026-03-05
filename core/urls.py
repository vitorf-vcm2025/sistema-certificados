from django.contrib import admin
from django.urls import path
# Importa a lógica que você criou
from certificados.views import detalhe_certificado

urlpatterns = [
    path('admin/', admin.site.urls),
    # Este é o link de validação que usa o UUID por segurança
    path('validar/<uuid:certificado_id>/',
         detalhe_certificado, name='detalhe_certificado'),
]
