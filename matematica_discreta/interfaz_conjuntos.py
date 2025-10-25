import tkinter as tk
from tkinter import messagebox
from logica import operar_conjuntos

def ventana_conjuntos():
    win = tk.Toplevel()
    win.title("Operaciones con Conjuntos")
    win.geometry("400x300")
    win.configure(bg="#ecf0f1")

    tk.Label(win, text="Conjunto A (a,b,c):", bg="#ecf0f1").pack()
    entry_a = tk.Entry(win)
    entry_a.pack()

    tk.Label(win, text="Conjunto B (a,b,c):", bg="#ecf0f1").pack()
    entry_b = tk.Entry(win)
    entry_b.pack()

    operacion = tk.StringVar()
    operacion.set("union")
    tk.OptionMenu(win, operacion, "union", "interseccion", "diferencia").pack(pady=10)

    resultado = tk.Label(win, text="", bg="#ecf0f1")
    resultado.pack()

    def calcular():
        try:
            conjunto_a = set(entry_a.get().split(","))
            conjunto_b = set(entry_b.get().split(","))
            op = operacion.get()
            res = operar_conjuntos(conjunto_a, conjunto_b, op)
            resultado.config(text=f"Resultado: {res}")
        except:
            messagebox.showerror("Error", "Entrada inválida. Separá los elementos con comas.")

    tk.Button(win, text="Calcular", command=calcular, bg="#e67e22", fg="white", width=30, height=2, font=('Arial', 10)).pack(pady=10)
