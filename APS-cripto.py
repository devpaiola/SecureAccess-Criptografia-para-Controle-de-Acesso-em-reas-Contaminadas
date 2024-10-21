# Funções de Criptografia
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
    criptografada = []
    for i in range(len(mensagem)):
        criptografada.append(ord(mensagem[i]) ^ ord(chave[i % len(chave)]))
    return criptografada  # Retorna a lista de valores decimais

def validar_chave(chave):
    if len(chave) < 12:
        print("Erro: A chave deve ter no mínimo 12 caracteres!")
        return False
    return True

# Interface principal do sistema
while True:
    print("\nBem-vindo ao Sistema de Controle de Acesso Sustentável!\n")
    print("Contexto: Um navio que transportava lixo tóxico da Ásia foi apreendido. Apenas inspetores autorizados com")
    print("equipamento de proteção adequado podem acessar áreas contaminadas do navio.")
    print("\nPara garantir a segurança, será necessário criptografar a senha de acesso.")
    
    print("\nEscolha o método de criptografia para proteger as credenciais:")
    print("1 - Cifra de Deslocamento (+5)")
    print("2 - XOR Cipher")
    metodo = input("Digite o número do método desejado: ")

    print("\nEscolha a ação que deseja realizar:")
    print("1 - Criptografar")
    print("2 - Descriptografar")
    case = input("Digite o número da ação desejada: ")

    if metodo == "1":
        chave = input("Entre com uma chave de segurança (mínimo 12 caracteres): ")
        if not validar_chave(chave):
            continue 

        if case == "1":
            text = input("\nInspetor, insira sua senha para criptografar o acesso: ")
            text_encriptaded = criptografar_deslocamento(text)
            print("\nSenha criptografada: ", text_encriptaded)

            with open("senha_criptografada_deslocamento.txt", "w") as file:
                file.write(f"Senha original: {text}\n")
                file.write(f"Chave de segurança: {chave}\n")
                file.write(f"Senha criptografada: {text_encriptaded}\n")
            print("Senha criptografada armazenada no arquivo 'senha_criptografada_deslocamento.txt'.")

        elif case == "2":
            text = input("\nInspetor, insira a senha criptografada para descriptografar: ")
            text_descriptaded = descriptografar_deslocamento(text)
            print("\nSenha descriptografada: ", text_descriptaded)

            with open("senha_descriptografada_deslocamento.txt", "w") as file:
                file.write(f"Senha criptografada: {text}\n")
                file.write(f"Chave de segurança: {chave}\n")
                file.write(f"Senha descriptografada: {text_descriptaded}\n")
            print("Senha descriptografada armazenada no arquivo 'senha_descriptografada_deslocamento.txt'.")

    elif metodo == "2":
        chave = input("Entre com uma chave de segurança (mínimo 12 caracteres): ")
        if not validar_chave(chave):
            continue

    if case == "1":
        text = input("\nInspetor, insira sua senha para criptografar o acesso: ")
        text_encriptaded = xor_cipher(text, chave)
        print("\nSenha criptografada (valores decimais): ", text_encriptaded)

        # Definir valores_decimais para armazenar corretamente no arquivo
        valores_decimais = text_encriptaded
        with open("senha_criptografada_xor.txt", "w") as file:
            file.write(f"Senha original: {text}\n")
            file.write(f"Chave de segurança: {chave}\n")
            file.write(f"Senha criptografada (valores decimais): {valores_decimais}\n")
        print("Senha criptografada armazenada no arquivo 'senha_criptografada_xor.txt'.")

    elif case == "2":
        # Para descriptografar, é necessário reverter a lista de valores decimais.
        text = input("\nInspetor, insira os valores decimais da senha criptografada, separados por espaço: ")
        # Remover vírgulas e converter para uma lista de inteiros
        valores_decimais = list(map(int, text.replace(',', '').split()))
        chave = input("Entre com a chave de segurança utilizada na criptografia: ")
        text_descriptaded = "".join(chr(val ^ ord(chave[i % len(chave)])) for i, val in enumerate(valores_decimais))
        print("\nSenha descriptografada: ", text_descriptaded)

        with open("senha_descriptografada_xor.txt", "w") as file:
            file.write(f"Senha criptografada (valores decimais): {valores_decimais}\n")
            file.write(f"Chave de segurança: {chave}\n")
            file.write(f"Senha descriptografada: {text_descriptaded}\n")
        print("Senha descriptografada armazenada no arquivo 'senha_descriptografada_xor.txt'.")


    else:
        print("\nOpção inválida! Por favor, tente novamente.")

    opcao = input("\nDigite 0 para sair ou 1 para voltar ao início: ")
    if opcao == "0":
        print("\nSaindo do sistema de controle de acesso sustentável... Até mais!")
        break
