import customtkinter as ctk #importando o CTk

window = ctk.CTk() #definindo janela
window.title('Login') #titulo da janela
window.geometry('800x600') #definindo tamanho da janela
window.maxsize(width=900, height=700) #tamanho maximo
window.minsize(width=800, height=600) #tamanho minimo
ctk.set_appearance_mode('dark') #tema da janela


window.mainloop() #loop que ira iniciar a janela
