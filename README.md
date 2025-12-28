# login-python
Sistema de login com Python

## O que esse projeto faz

Este projeto é um **sistema de login gráfico** feito em Python usando **CustomTkinter**, uma versão modernizada do Tkinter.  
A aplicação mostra uma janela com:

- Título “Sistema de Login”  
- Campo de usuário  
- Campo de senha (com caracteres escondidos)  
- Botão de login  
- Mensagem de feedback (sucesso ou erro)  

Quando o usuário digita as credenciais corretas, aparece uma mensagem de sucesso na tela e também uma janela informando que o login deu certo.

***

## Como o código está organizado

### 1. Imports e tema da interface

```python
import customtkinter as ctk
import tkinter.messagebox as mb

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
```

- `customtkinter` é a biblioteca usada para criar a interface moderna.  
- `tkinter.messagebox` é usado para exibir janelas pop-up (como “Sucesso” ou “Erro”).  
- `set_appearance_mode("dark")` define o tema escuro.  
- `set_default_color_theme("blue")` define o tema de cores azul.

---

### 2. Janela principal

```python
app = ctk.CTk()
app.title("Sistema de Login")
app.geometry("300x280")
app.resizable(False, False)
```

- Cria a **janela principal** (`CTk`).  
- Define o título que aparece na barra da janela.  
- Define o tamanho da tela (largura x altura).  
- `resizable(False, False)` impede que o usuário redimensione a janela.

---

### 3. Usuário e senha “corretos”

```python
USUARIO_CORRETO = "lucas"
SENHA_CORRETA = "123456"
```

- Aqui estão os **dados fixos** usados para validar o login.  
- Em um sistema real, isso poderia vir de um banco de dados, arquivo ou API.

---

### 4. Função de validação do login

```python
def validar_login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    if usuario == USUARIO_CORRETO and senha == SENHA_CORRETA:
        label_resultado.configure(
            text="Login feito com sucesso!",
            text_color="green"
        )
        mb.showinfo("Sucesso", "Você entrou no sistema!")
    else:
        label_resultado.configure(
            text="Login incorreto!",
            text_color="red"
        )
```

- A função é chamada quando o usuário clica no botão **Login**.  
- Ela pega o texto digitado nos campos de usuário e senha.  
- Se bater com os valores definidos (`USUARIO_CORRETO` e `SENHA_CORRETA`):
  - Atualiza o rótulo na tela com uma mensagem de sucesso em verde.  
  - Abre uma janela pop-up (`showinfo`) informando que o login foi bem-sucedido.  
- Se estiver errado:
  - Mostra “Login incorreto!” em vermelho na própria janela.

***

### 5. Criação dos elementos da interface (widgets)

Abaixo são criados todos os componentes da tela, um por um, e organizados com `pack()`.

#### Título

```python
label_titulo = ctk.CTkLabel(
    app,
    text="Sistema de Login",
    font=("Arial", 18, "bold")
)
label_titulo.pack(pady=15)
```

- Rótulo no topo, com texto maior e em negrito, para ser o título da tela.

#### Campo de usuário

```python
label_usuario = ctk.CTkLabel(
    app,
    text="Usuário:"
)
label_usuario.pack(pady=(5, 0))

entry_usuario = ctk.CTkEntry(
    app,
    placeholder_text="Digite seu usuário"
)
entry_usuario.pack(pady=5)
```

- Um rótulo “Usuário:” e um campo de entrada logo abaixo.  
- O `placeholder_text` ajuda o usuário, mostrando um texto de exemplo dentro do campo.

#### Campo de senha

```python
label_senha = ctk.CTkLabel(
    app,
    text="Senha:"
)
label_senha.pack(pady=(10, 0))

entry_senha = ctk.CTkEntry(
    app,
    placeholder_text="Digite sua senha",
    show="*"
)
entry_senha.pack(pady=5)
```

- Mesma ideia do usuário, mas para a senha.  
- A diferença é o `show="*"`, que faz a senha aparecer como asteriscos, e não como texto puro.

#### Botão de login

```python
botao_login = ctk.CTkButton(
    app,
    text="Login",
    command=validar_login
)
botao_login.pack(pady=15)
```

- Botão que o usuário clica para tentar entrar.  
- `command=validar_login` conecta o botão à função definida antes.  
- Quando clicado, executa a lógica de validação.

#### Mensagem de resultado

```python
label_resultado = ctk.CTkLabel(
    app,
    text="",
    font=("Arial", 12)
)
label_resultado.pack(pady=5)
```

- Rótulo inicialmente vazio.  
- Ele é atualizado pela função `validar_login` para mostrar se o login deu certo ou errado.

---

### 6. Loop da aplicação

```python
app.mainloop()
```

- Inicia o **loop principal** da interface.  
- A partir daqui, a janela fica aberta esperando cliques, digitação etc.

***

## Como executar

1. Tenha o Python instalado.  
2. Instale o CustomTkinter:

   ```bash
   pip install customtkinter
   ```

3. Salve o código em um arquivo, por exemplo: `login.py`.  
4. Rode:

   ```bash
   python login.py
   ```

A janela do sistema de login será aberta.  
Usuário padrão: `lucas`  
Senha padrão: `123456`  

Você pode editar essas credenciais no topo do arquivo (`USUARIO_CORRETO` e `SENHA_CORRETA`) para adaptar ao seu caso.
