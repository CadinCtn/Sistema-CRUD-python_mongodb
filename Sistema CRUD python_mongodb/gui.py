import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from pcconfig import PC_config
from database import conectar_mongo

class PCApp:
    def __init__(self, root):
        self.db = conectar_mongo()
        self.pc_config = PC_config(self.db)
        
        self.root = root
        self.root.title("Registro de Configurações de computadores")
        self.root.geometry("600x600")

        #Widgets
        self.id_label = ttk.Label(root, text="Cod. Identificador: ")
        self.id_label.grid(row=0, column=0, padx=5, pady=5)
        self.id_entry = ttk.Entry(root)
        self.id_entry.grid(row=0, column=1, padx=5, pady=5)

        self.processador_label = ttk.Label(root, text="Processador: ")
        self.processador_label.grid(row=1, column=0, padx=5, pady=5)
        self.processador_entry = ttk.Entry(root)
        self.processador_entry.grid(row=1, column=1, padx=5, pady=5)

        self.memoria_label = ttk.Label(root, text="Memoria Ram: ")
        self.memoria_label.grid(row=2, column=0, padx=5, pady=5)
        self.memoria_entry = ttk.Entry(root)
        self.memoria_entry.grid(row=2, column=1, padx=5, pady=5)

        self.armazenamento_label = ttk.Label(root, text="Armazenamento: ")
        self.armazenamento_label.grid(row=3, column=0, padx=5, pady=5)
        self.armazenamento_entry = ttk.Entry(root)
        self.armazenamento_entry.grid(row=3, column=1, padx=5, pady=5)

        self.placa_video_label = ttk.Label(root, text="Placa de video: ")
        self.placa_video_label.grid(row=4, column=0, padx=5, pady=5)
        self.placa_video_entry = ttk.Entry(root)
        self.placa_video_entry.grid(row=4, column=1, padx=5, pady=5)

        self.placa_mae_label = ttk.Label(root, text="Placa de Mãe: ")
        self.placa_mae_label.grid(row=5, column=0, padx=5, pady=5)
        self.placa_mae_entry = ttk.Entry(root)
        self.placa_mae_entry.grid(row=5, column=1, padx=5, pady=5)


        self.btn_add = ttk.Button(root, text="Inserir item", command=self.adicionar_item)
        self.btn_add.grid(row=6, column=0, padx=5, pady=5)

        self.btn_del = ttk.Button(root, text="Remover item", command=self.remover_item)
        self.btn_del.grid(row=6, column=1, padx=5, pady=5)

        self.btn_listar = ttk.Button(root, text="Lista itens", command=self.listar_itens)
        self.btn_listar.grid(row=7, column=0, padx=5, pady=5)

        self.resultado_text = tk.Text(root, height=10, width=40)
        self.resultado_text.grid(row=8, column=0, columnspan=2, padx=5, pady=5)
        
    def clear_fields(self):
        self.id_entry.delete(0, tk.END)
        self.processador_entry.delete(0, tk.END)
        self.memoria_entry.delete(0, tk.END)
        self.armazenamento_entry.delete(0, tk.END)
        self.placa_video_entry.delete(0, tk.END)
        self.placa_mae_entry.delete(0, tk.END)

    def adicionar_item(self):
        id = self.id_entry.get()
        processador = self.processador_entry.get()
        memoria_ram = self.memoria_entry.get()
        armazenamento = self.armazenamento_entry.get
        placa_video = self.placa_video_entry.get()
        placa_mae = self.placa_mae_entry.get()

        if self.pc_config.add_config(id, processador, memoria_ram, armazenamento, placa_video, placa_mae):
            messagebox.showinfo("Sucesso", "Configuração inserida com sucesso!")
            self.clear_fields()
            self.listar_itens()
        else:
            messagebox.showerror("ERRO", "Não foi possivel inserir a configuração")
        

    def remover_item(self):
        id = self.id_entry.get()
        if self.pc_config.del_config(id):
            messagebox.showinfo("Sucesso", "Configuração removida com sucesso!")
            self.clear_fields()
            self.listar_itens()
        else:
            messagebox.showinfo("Não encontrado", "Não foi possivel encontrar a configuração")
            
    def listar_itens(self):
        self.resultado_text.delete(1.0, tk.END)
        configs = self.pc_config.listar_config()
        for config in configs:
            self.resultado_text.insert(tk.END, f"{config['id']}\n {config['processador']}\n {config['memoria_ram']}\n {config['armazenamento']}\n {config['placa_video']}\n {config['placa_mae']}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PCApp(root)
    root.mainloop()