import tkinter as tk
from tkinter import messagebox
from logica import calcular_permutacion

def ventana_permutaciones():
    win = tk.Toplevel()
    win.title("Permutaciones")
    win.geometry("300x250")
    win.configure(bg="#ecf0f1")

    tk.Label(win, text="n:", font=('Arial', 12), bg="#ecf0f1").pack(pady=5)
    entry_n = tk.Entry(win)
    entry_n.pack()

    tk.Label(win, text="r:", font=('Arial', 12), bg="#ecf0f1").pack(pady=5)
    entry_r = tk.Entry(win)
    entry_r.pack()

    resultado = tk.Label(win, text="", bg="#ecf0f1", font=('Arial', 12))
    resultado.pack(pady=10)

    def calcular():
        try:
            n = int(entry_n.get())
            r = int(entry_r.get())
            res = calcular_permutacion(n, r)
            resultado.config(text=f"Resultado: {res}")
        except:
            messagebox.showerror("Error", "Ingresa valores enteros válidos.")

    tk.Button(win, text="Calcular", command=calcular, bg="#9b59b6", fg="white").pack(pady=10)
