def criptografar_deslocamento(key):
    mensagem = ""
    for i in key:
        mensagem += chr(ord(i) + 5)
    return mensagem

def descriptografar_deslocamento(key):
    mensagem = ""
    for i in key:
        mensagem += chr(ord(i) - 5)
    return mensagem

def xor_cipher(mensagem, chave):
    criptografada = ""
    for i in range(len(mensagem)):
        criptografada += chr(ord(mensagem[i]) ^ ord(chave[i % len(chave)]))
    return criptografada

def validar_chave(chave):
    if len(chave) < 12:
        print("Erro: A chave deve ter no mínimo 12 caracteres!")
        return False
    return True

while True:
    print("\nBem-vindo ao programa de criptografia! ASC2")
    
    print("Escolha o método de criptografia:")
    print("1 - Cifra de Deslocamento (+5)")
    print("2 - XOR Cipher")
    metodo = input("Digite o número do método desejado: ")

    case = input("Digite 1 para criptografar e 2 para descriptografar: ")

    if metodo == "1":
        chave = input("Entre com a chave (mínimo 12 caracteres): ")
        if not validar_chave(chave):
            continue 
        
        if case == "1":
            text = input("Entre com a mensagem para ser criptografada: ")
            text_encriptaded = criptografar_deslocamento(text)
            print("Mensagem criptografada: ", text_encriptaded)

            with open("mensagem_criptografada_deslocamento.txt", "w") as file:
                file.write(f"Mensagem original: {text}\n")
                file.write(f"Chave: {chave}\n")
                file.write(f"Mensagem criptografada: {text_encriptaded}\n")
            print("Mensagem criptografada armazenada no arquivo 'mensagem_criptografada_deslocamento.txt'.")

        elif case == "2":
            text = input("Entre com a mensagem para ser descriptografada: ")
            text_descriptaded = descriptografar_deslocamento(text)
            print("Mensagem descriptografada: ", text_descriptaded)

            with open("mensagem_descriptografada_deslocamento.txt", "w") as file:
                file.write(f"Mensagem criptografada: {text}\n")
                file.write(f"Chave: {chave}\n")
                file.write(f"Mensagem descriptografada: {text_descriptaded}\n")
            print("Mensagem descriptografada armazenada no arquivo 'mensagem_descriptografada_deslocamento.txt'.")

    elif metodo == "2":
        chave = input("Entre com a chave de criptografia (mínimo 12 caracteres): ")
        if not validar_chave(chave):
            continue 

        if case == "1":
            text = input("Entre com a mensagem para ser criptografada: ")
            text_encriptaded = xor_cipher(text, chave)
            print("Mensagem criptografada: ", text_encriptaded)

            with open("mensagem_criptografada_xor.txt", "w") as file:
                file.write(f"Mensagem original: {text}\n")
                file.write(f"Chave de criptografia: {chave}\n")
                file.write(f"Mensagem criptografada: {text_encriptaded}\n")
            print("Mensagem criptografada armazenada no arquivo 'mensagem_criptografada_xor.txt'.")

        elif case == "2":
            text = input("Entre com a mensagem para ser descriptografada: ")
            text_descriptaded = xor_cipher(text, chave)
            print("Mensagem descriptografada: ", text_descriptaded)

            with open("mensagem_descriptografada_xor.txt", "w") as file:
                file.write(f"Mensagem criptografada: {text}\n")
                file.write(f"Chave de criptografia: {chave}\n")
                file.write(f"Mensagem descriptografada: {text_descriptaded}\n")
            print("Mensagem descriptografada armazenada no arquivo 'mensagem_descriptografada_xor.txt'.")

    else:
        print("Opção inválida! Tente novamente.")

    opcao = input("\nDigite 0 para sair ou 1 para voltar ao início: ")
    if opcao == "0":
        print("Saindo do programa...")
        break
