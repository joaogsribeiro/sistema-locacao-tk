import tkinter as tk
from gui.cadastro_equipamento import mostrar_tela_cadastro
from gui.lista_equipamentos import mostrar_tela_listagem

def criar_tela_principal():
    janela = tk.Tk()
    janela.title("Sistema de Locação")
    janela.geometry("400x300")

    container = tk.Frame(janela)
    container.pack(fill="both", expand=True)

    def ir_para_cadastro():
        for widget in container.winfo_children():
            widget.destroy()
        mostrar_tela_cadastro(container)

    titulo = tk.Label(container, text="Menu Principal", font=("Arial", 16))
    titulo.pack(pady=20)

    botao_listar = tk.Button(container, text="Listar Equipamentos", command=lambda: mostrar_tela_listagem(container), width=25)
    botao_listar.pack(pady=10)

    botao_cadastro = tk.Button(container, text="Cadastrar Equipamento", command=ir_para_cadastro, width=25)
    botao_cadastro.pack(pady=10)

    janela.mainloop()
