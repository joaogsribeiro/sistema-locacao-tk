import tkinter as tk
from tkinter import messagebox
from database import conectar
from gui.cadastro_equipamento import mostrar_tela_cadastro

def listar_equipamentos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM equipamentos')
    dados = cursor.fetchall()
    conn.close()
    return dados

def excluir_equipamento(id_equip):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute('DELETE FROM equipamentos WHERE id = ?', (id_equip,))
        conn.commit()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao excluir: {e}")
    finally:
        conn.close()

def mostrar_tela_listagem(frame):
    for widget in frame.winfo_children():
        widget.destroy()

    tk.Label(frame, text="Equipamentos Cadastrados", font=("Arial", 14)).grid(row=0, column=0, columnspan=5, pady=10)

    colunas = ["ID", "Nome", "Descrição", "Qtd", "Valor/Dia", "Ações"]
    for i, nome_col in enumerate(colunas):
        tk.Label(frame, text=nome_col, font=("Arial", 10, "bold")).grid(row=1, column=i, padx=5, pady=5)

    equipamentos = listar_equipamentos()

    for idx, eq in enumerate(equipamentos, start=2):
        tk.Label(frame, text=eq[0]).grid(row=idx, column=0)
        tk.Label(frame, text=eq[1]).grid(row=idx, column=1)
        tk.Label(frame, text=eq[2]).grid(row=idx, column=2)
        tk.Label(frame, text=eq[3]).grid(row=idx, column=3)
        tk.Label(frame, text=f"R$ {eq[4]:.2f}").grid(row=idx, column=4)

        def criar_callback_editar(equipamento=eq):
            return lambda: mostrar_tela_cadastro(frame, equipamento)

        def criar_callback_excluir(eid=eq[0]):
            return lambda: [
                excluir_equipamento(eid),
                mostrar_tela_listagem(frame)
            ]

        # editar: podemos conectar à mesma tela de cadastro no futuro
        tk.Button(frame, text="Editar", command=criar_callback_editar()).grid(row=idx, column=5)
        tk.Button(frame, text="Excluir", command=criar_callback_excluir()).grid(row=idx, column=6)

    def ir_para_cadastro():
        mostrar_tela_cadastro(frame)

    tk.Button(frame, text="Cadastrar Novo Equipamento", command=ir_para_cadastro).grid(row=idx + 1, column=0, columnspan=7, pady=15)
