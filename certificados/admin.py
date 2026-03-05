from django.contrib import admin
from . models import Aluno, Curso, Certificado


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'cpf', 'email')
    search_fields = ('nome_completo', 'cpf')


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'carga_horaria')


@admin.register(Certificado)
class CertificadoAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'curso', 'data_emissao', 'chave_validacao')
    # Segurança: ninguém altera a chave na mão!
    readonly_fields = ('chave_validacao', )
