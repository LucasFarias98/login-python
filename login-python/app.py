import customtkinter as ctk
import tkinter.messagebox as mb  




ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


app = ctk.CTk()
app.title("Sistema de Login")
app.geometry("300x280")  # largura x altura
app.resizable(False, False)


USUARIO_CORRETO = "lucas"
SENHA_CORRETA = "123456"


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


label_titulo = ctk.CTkLabel(
    app,
    text="Sistema de Login",
    font=("Arial", 18, "bold")
)
label_titulo.pack(pady=15)


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


botao_login = ctk.CTkButton(
    app,
    text="Login",
    command=validar_login
)
botao_login.pack(pady=15)


label_resultado = ctk.CTkLabel(
    app,
    text="",
    font=("Arial", 12)
)
label_resultado.pack(pady=5)


app.mainloop()
