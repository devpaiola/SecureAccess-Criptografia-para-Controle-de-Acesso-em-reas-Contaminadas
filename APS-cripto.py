import tkinter as tk
from tkinter import messagebox

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
        messagebox.showerror("Erro", "A chave deve ter no mínimo 12 caracteres!")
        return False
    return True

# Funções para o UI
def executar_criptografia():
    metodo = metodo_var.get()
    acao = acao_var.get()
    chave = entrada_chave.get()
    texto = entrada_texto.get()

    if not validar_chave(chave):
        return

    if metodo == "deslocamento":
        if acao == "criptografar":
            resultado = criptografar_deslocamento(texto)
            salvar_arquivo("senha_criptografada_deslocamento.txt", texto, chave, resultado)
            messagebox.showinfo("Resultado", f"Senha criptografada: {resultado}")
        elif acao == "descriptografar":
            resultado = descriptografar_deslocamento(texto)
            salvar_arquivo("senha_descriptografada_deslocamento.txt", texto, chave, resultado)
            messagebox.showinfo("Resultado", f"Senha descriptografada: {resultado}")

    elif metodo == "xor":
        if acao == "criptografar":
            resultado = xor_cipher(texto, chave)
            resultado_str = ', '.join(map(str, resultado))
            salvar_arquivo("senha_criptografada_xor.txt", texto, chave, resultado_str)
            messagebox.showinfo("Resultado", f"Senha criptografada (decimais): {resultado_str}")
        elif acao == "descriptografar":
            try:
                valores_decimais = list(map(int, texto.split(',')))
                resultado = "".join(chr(val ^ ord(chave[i % len(chave)])) for i, val in enumerate(valores_decimais))
                salvar_arquivo("senha_descriptografada_xor.txt", texto, chave, resultado)
                messagebox.showinfo("Resultado", f"Senha descriptografada: {resultado}")
            except ValueError:
                messagebox.showerror("Erro", "Formato inválido! Digite os valores decimais separados por vírgulas.")

def salvar_arquivo(nome_arquivo, original, chave, resultado):
    with open(nome_arquivo, "w") as file:
        file.write(f"Senha original: {original}\n")
        file.write(f"Chave de segurança: {chave}\n")
        file.write(f"Resultado: {resultado}\n")
    messagebox.showinfo("Salvo", f"Resultado salvo no arquivo '{nome_arquivo}'.")

# Interface Tkinter
root = tk.Tk()
root.title("Sistema de Controle de Acesso Sustentável")
root.geometry("400x300")

# Labels e Entradas
tk.Label(root, text="Chave de Segurança (mínimo 12 caracteres):").pack(pady=5)
entrada_chave = tk.Entry(root, width=30)
entrada_chave.pack(pady=5)

tk.Label(root, text="Texto (Senha):").pack(pady=5)
entrada_texto = tk.Entry(root, width=30)
entrada_texto.pack(pady=5)

# Opções de Método e Ação
metodo_var = tk.StringVar(value="deslocamento")
acao_var = tk.StringVar(value="criptografar")

tk.Label(root, text="Método de Criptografia:").pack(pady=5)
tk.Radiobutton(root, text="Cifra de Deslocamento (+5)", variable=metodo_var, value="deslocamento").pack()
tk.Radiobutton(root, text="XOR Cipher", variable=metodo_var, value="xor").pack()

tk.Label(root, text="Ação:").pack(pady=5)
tk.Radiobutton(root, text="Criptografar", variable=acao_var, value="criptografar").pack()
tk.Radiobutton(root, text="Descriptografar", variable=acao_var, value="descriptografar").pack()

# Botão Executar
tk.Button(root, text="Executar", command=executar_criptografia).pack(pady=20)

root.mainloop()
