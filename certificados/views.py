from django.shortcuts import render, get_object_or_404
from .models import Certificado
import qrcode
import io
import base64
from django.contrib.auth.decorators import login_required


def detalhe_certificado(request, id_seguranca):
    certificado = get_object_or_404(Certificado, id=id_seguranca)

    meu_ip = "192.168.0.196"
    link_validacao = f"http://{meu_ip}:8000/validar/{id_seguranca}/"

    # Cria o QR Code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(link_validacao)
    qr.make(fit=True)

    # Transforma a imagem em texto (base64) para o HTML ler
    img = qr.make_image(fill_color="black", back_color="white")
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    qr_base64 = base64.b64encode(buffer.getvalue()).decode()

    contexto = {
        'certificado': certificado,
        'qr_code': qr_base64
    }

    return render(request, 'certificados/detalhe.html', contexto)


@login_required
def lista_certificados(request):
    """
    Lista os certificados e permite filtrar por nome do aluno.
    """
    # 1. Pega o termo que o usuário digitou na busca
    termo_busca = request.GET.get('busca')

    # 2. Começa com todos os certificados
    certificados = Certificado.objects.all().order_by('-data_emissao')

    # 3. Se houver algo na busca, filtra os resultados
    if termo_busca:
        certificados = certificados.filter(
            aluno__nome_completo__icontains=termo_busca)

    return render(request, 'certificados/lista.html', {'certificados': certificados})
