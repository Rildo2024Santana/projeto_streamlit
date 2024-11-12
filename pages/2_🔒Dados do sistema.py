import tkinter as tk
from tkinter import messagebox

class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class SistemaCadastro:
    def __init__(self, root):
        self.clientes = []
        self.root = root
        self.root.title("Cadastro de Clientes")
        
        self.label_nome = tk.Label(root, text="Nome do Cliente:")
        self.label_nome.grid(row=0, column=0)
        self.entry_nome = tk.Entry(root)
        self.entry_nome.grid(row=0, column=1)
        
        self.label_email = tk.Label(root, text="Email do Cliente:")
        self.label_email.grid(row=1, column=0)
        self.entry_email = tk.Entry(root)
        self.entry_email.grid(row=1, column=1)
        
        self.botao_adicionar = tk.Button(root, text="Adicionar Cliente", c
        self.botao_adicionar.grid(row=2, column=0, columnspan=2)
        
        self.botao_listar = tk.Button(root, text="Listar Clientes", comman
        self.botao_listar.grid(row=3, column=0, columnspan=2)
        
        self.lista_clientes = tk.Text(root, height=10, width=50)
        self.lista_clientes.grid(row=4, column=0, columnspan=2)

    def adicionar_cliente(self):
        nome = self.entry_nome.get()
        email = self.entry_email.get()
        if nome and email:
            cliente = Cliente(nome, email)
            self.clientes.append(cliente)
            messagebox.showinfo("Sucesso", f"Cliente {nome} adicionado com
            self.entry_nome.delete(0, tk.END)
            self.entry_email.delete(0, tk.END)
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os cam

    def listar_clientes(self):
        self.lista_clientes.delete(1.0, tk.END)
        for cliente in self.clientes:
            self.lista_clientes.insert(tk.END, f'Nome: {cliente.nome}, Ema

root = tk.Tk()
sistema = SistemaCadastro(root)
root.mainloop()
