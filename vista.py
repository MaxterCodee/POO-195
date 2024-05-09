import tkinter as tk
import tkinter.messagebox as tkmb  # Cambiar esto
from logica import clogica

class cvista:
    def __init__(self, master):
        self.master = master
        self.logic = clogica()

        self.label = tk.Label(master, text="Manejo de Excepciones")
        self.label.pack()

        self.button = tk.Button(master, text="Generar Excepción", command=self.generate_exception)
        self.button.pack()

    def generate_exception(self):
        try:
            self.logic.generate_exception()
        except SyntaxError as e:
            tk.messagebox.showerror("Error", str(e))
