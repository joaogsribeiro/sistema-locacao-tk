import tkinter as tk
from tkinter import messagebox
from database import conectar

def cadastrar_equipamento(nome, descricao, qtd, valor):
    conn = conectar()
    cursor = conn.cursor()

    try:
        cursor.execute(
            'INSERT INTO equipamentos (nome, descricao, qtd_disponivel, valor_dia) VALUES (?, ?, ?, ?)',
            (nome, descricao, qtd, valor)
        )
        conn.commit()
        messagebox.showinfo("Sucesso", "Equipamento cadastrado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao cadastrar: {e}")
    finally:
        conn.close()

def mostrar_tela_cadastro(frame):
    for widget in frame.winfo_children():
        widget.destroy()

    tk.Label(frame, text="Cadastro de Equipamento", font=("Arial", 14)).grid(row=0, column=0, columnspan=2, pady=10)

    tk.Label(frame, text="Nome:").grid(row=1, column=0, sticky="e", padx=10, pady=5)
    nome_entry = tk.Entry(frame)
    nome_entry.grid(row=1, column=1)

    tk.Label(frame, text="Descrição:").grid(row=2, column=0, sticky="e", padx=10, pady=5)
    desc_entry = tk.Entry(frame)
    desc_entry.grid(row=2, column=1)

    tk.Label(frame, text="Quantidade disponível:").grid(row=3, column=0, sticky="e", padx=10, pady=5)
    qtd_entry = tk.Entry(frame)
    qtd_entry.grid(row=3, column=1)

    tk.Label(frame, text="Valor por dia (R$):").grid(row=4, column=0, sticky="e", padx=10, pady=5)
    valor_entry = tk.Entry(frame)
    valor_entry.grid(row=4, column=1)

    def ao_clicar():
        try:
            nome = nome_entry.get()
            descricao = desc_entry.get()
            qtd = int(qtd_entry.get())
            valor = float(valor_entry.get())
            cadastrar_equipamento(nome, descricao, qtd, valor)
            nome_entry.delete(0, tk.END)
            desc_entry.delete(0, tk.END)
            qtd_entry.delete(0, tk.END)
            valor_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Erro", "Quantidade deve ser inteiro e valor deve ser decimal.")

    tk.Button(frame, text="Cadastrar", command=ao_clicar).grid(row=5, column=0, columnspan=2, pady=15)
