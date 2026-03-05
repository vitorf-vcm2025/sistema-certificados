from django.shortcuts import render, get_object_or_404
from .models import Certificado
import qrcode
import io
import base64


def detalhe_certificado(request, certificado_id):
    certificado = get_object_or_404(Certificado, id=certificado_id)

    meu_ip = "192.168.0.196"
    link_validacao = f"http://{meu_ip}:8000/validar/{certificado_id}/"

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


def lista_certificados(request):
    """
    Busca todos os certificados no banco de dados e exibe em uma lista.
    """
    todos_certificados = Certificado.objects.all().order_by('-data_emissao')

    return render(request, 'certificados/lista.html', {'certificados': todos_certificados})
