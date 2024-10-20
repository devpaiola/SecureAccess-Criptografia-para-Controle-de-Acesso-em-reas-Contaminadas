
# Controle de Acesso - Sustentabilidade

Este projeto é um sistema de controle de acesso que utiliza criptografia para proteger informações sensíveis. O cenário envolve restrição de acesso a uma área contaminada ambientalmente, permitindo que apenas inspetores autorizados acessem o local, usando uma senha criptografada.

## Funcionalidades

O sistema oferece dois métodos de criptografia e descriptografia de mensagens:
1. **Cifra de Deslocamento (+5)**: A mensagem é criptografada deslocando cada caractere em +5 posições na tabela ASCII.
2. **XOR Cipher**: A mensagem é criptografada usando a operação XOR (bit a bit) com uma chave fornecida pelo usuário.

Ambos os métodos podem ser usados para criptografar ou descriptografar uma mensagem.

### Principais Funcionalidades:
- Validação da chave de criptografia: A chave deve ter no mínimo 12 caracteres.
- Criptografia/Descriptografia usando Cifra de Deslocamento (+5).
- Criptografia/Descriptografia usando XOR Cipher.
- Armazenamento de mensagens criptografadas e descriptografadas em arquivos `.txt`.

## Requisitos do Sistema

Este código é escrito em **Python** e pode ser executado em qualquer ambiente Python com a versão 3.x ou superior.

### Requisitos de execução:
- **Python 3.x**

## Como usar

1. **Baixe ou clone o repositório para o seu computador.**
2. **Execute o script `controle_acesso.py`.**
   
   ```bash
   python controle_acesso.py
   ```

3. O programa exibirá o menu principal, onde você deverá:
   - Escolher o método de criptografia desejado (1 - Cifra de Deslocamento ou 2 - XOR Cipher).
   - Escolher se deseja criptografar ou descriptografar uma mensagem.
   - Inserir a chave de criptografia (mínimo de 12 caracteres).
   - Inserir a mensagem para ser criptografada ou descriptografada.
   - O programa salva as mensagens em arquivos `.txt` para fácil consulta posterior.

### Exemplo de uso:

- Para criptografar uma mensagem usando **Cifra de Deslocamento (+5)**:
  - Escolha o método 1.
  - Escolha a opção 1 para criptografar.
  - Insira uma chave válida (mínimo 12 caracteres).
  - Insira a mensagem a ser criptografada.
  - A mensagem criptografada será exibida no terminal e também será salva no arquivo `mensagem_criptografada_deslocamento.txt`.

- Para criptografar uma mensagem usando **XOR Cipher**:
  - Escolha o método 2.
  - Escolha a opção 1 para criptografar.
  - Insira uma chave válida (mínimo 12 caracteres).
  - Insira a mensagem a ser criptografada.
  - A mensagem criptografada será exibida no terminal e também será salva no arquivo `mensagem_criptografada_xor.txt`.

## Estrutura do Projeto

```
controle_acesso.py   # Script principal com todo o código do programa
mensagem_criptografada_deslocamento.txt  # Arquivo gerado para a Cifra de Deslocamento
mensagem_descriptografada_deslocamento.txt  # Arquivo gerado para descriptografia da Cifra de Deslocamento
mensagem_criptografada_xor.txt  # Arquivo gerado para a criptografia XOR
mensagem_descriptografada_xor.txt  # Arquivo gerado para descriptografia XOR
```

## Funcionamento do Código

- **Cifra de Deslocamento (+5)**:
  - A função `criptografar_deslocamento(key)` percorre cada caractere da mensagem e altera sua posição na tabela ASCII, somando 5 ao valor ordinal.
  - A função `descriptografar_deslocamento(key)` faz o processo inverso, subtraindo 5 do valor ordinal para reverter a criptografia.

- **XOR Cipher**:
  - A função `xor_cipher(mensagem, chave)` realiza a operação XOR entre o valor ASCII de cada caractere da mensagem e o valor correspondente da chave. Se a chave for menor que a mensagem, ela é repetida ciclicamente.

- **Validação da chave**:
  - A função `validar_chave(chave)` verifica se a chave tem pelo menos 12 caracteres, alertando o usuário caso não seja.

- **Arquivos gerados**:
  - As mensagens criptografadas e descriptografadas são armazenadas em arquivos `.txt` para referência futura.

## Considerações Finais

- Este código é ideal para pequenos projetos de controle de acesso e demonstra conceitos básicos de criptografia.
- A implementação da criptografia é simples e pode ser expandida para incluir outros algoritmos.
- A validação da chave garante uma segurança mínima exigida, mas você pode aprimorá-la conforme necessário.

---

## Contribuições

Sinta-se à vontade para enviar _pull requests_ ou abrir _issues_ se encontrar problemas ou tiver sugestões para melhorias.

## Licença

Este projeto é de código aberto e está disponível sob a licença MIT.

---

## Autor

**Fabricio Paiola G dos Santos**
**Pedro Henrique P. Onório** 
Cientistas da computação  
Desenvolvedor apaixonado por criptografia e sustentabilidade

