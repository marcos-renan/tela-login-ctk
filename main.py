import customtkinter as ctk #importando o CTk

#Funçao para validar senha e email
def validar_login():
  usuario = campo_usuario.get()
  senha = campo_senha.get()

  #Verificar se email é marcos e senha = 123456
  if usuario == 'marcos' and senha == '123456':
    result_login.configure(text='Login feito com sucesso!', text_color='green')
  else:
    result_login.configure(text='Usuário ou senha inválidos.', text_color='red')


window = ctk.CTk() #definindo janela
window.title('Login') #titulo da janela
window.geometry('300x300') #definindo tamanho da janela
window.maxsize(width=300, height=300) #tamanho maximo
window.minsize(width=300, height=300) #tamanho minimo
ctk.set_appearance_mode('dark') #tema da janela

#Campos

#Label
label_usuario = ctk.CTkLabel(window, text='Usuário')
label_usuario.pack(pady=10)

#Entry
campo_usuario = ctk.CTkEntry(window, placeholder_text='Digite seu usuário')
campo_usuario.pack(pady=10)

#Label
label_senha = ctk.CTkLabel(window, text='Senha')
label_senha.pack(pady=10)

#Entry
campo_senha = ctk.CTkEntry(window, placeholder_text='Digite sua senha', show='*')
campo_senha.pack(pady=10)

#Button
botao_login = ctk.CTkButton(window, text='Entrar', command=validar_login)
botao_login.pack(pady=10)

#campo de feedback do login
result_login = ctk.CTkLabel(window, text='')
result_login.pack(pady=10)

window.mainloop() #loop que ira iniciar a janela
