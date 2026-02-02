import qrcode

def gerador_qrcode(dados, nome_arquivo):
    # Cria uma instância do objeto QRCode
    qr = qrcode.QRCode(
        version=1,  # controla o tamanho do QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # controla a correção de erros
        box_size=10,  # tamanho de cada caixa do QR Code
        border=4,  # largura da borda
    )
    
    # Adiciona os dados ao QR Code
    qr.add_data(dados)
    qr.make(fit=True)
    
    # Cria uma imagem do QR Code
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Salva a imagem em um arquivo
    img.save(nome_arquivo)
    
    #Mostra a imagem do QR Code
    img.show()

# Solicita ao usuário os dados e o nome do arquivo
dados = str(input("Digite os dados para o QR Code: "))
nome_arquivo = str(input("Digite o nome do arquivo para salvar o QR Code (ex: qrcode.png): "))


gerador_qrcode(dados, nome_arquivo)
