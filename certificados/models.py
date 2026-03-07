import uuid
from django.db import models


class Aluno(models.Model):
    id_seguranca = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    nome_completo = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome_completo


class Curso(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=255)
    carga_horaria = models.PositiveIntegerField()

    def __str__(self):
        return self.nome


class Certificado(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    data_emissao = models.DateTimeField(auto_now_add=True)
    chave_validacao = models.CharField(
        max_length=50, unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.chave_validacao:
            self.chave_validacao = str(uuid.uuid4().hex[:10]).upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Certificado {self.aluno.nome_completo} - {self.curso.nome}"
