import tkinter as tk
from tkinter import messagebox
from logica import calcular_combinacion_sin_repeticion

def ventana_combinaciones():
    win = tk.Toplevel()
    win.title("Combinaciones")
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

    def calcular1():
        try:
            n = int(entry_n.get())
            r = int(entry_r.get())
            res = calcular_combinacion_sin_repeticion(n, r)
            resultado.config(text=f"Resultado: {res}")
        except:
            messagebox.showerror("Error", "Ingresá valores enteros válidos.")

    tk.Button(win, text="Calcular sin repeticion", command=calcular1, bg="#3498db", fg="white").pack(pady=10)

    def calcular2():
        try:
            n = int(entry_n.get())
            r = int(entry_r.get())
            res = calcular_combinacion_sin_repeticion(n + r - 1, r)
            resultado.config(text=f"Resultado: {res}")
        except:
            messagebox.showerror("Error", "Ingresá valores enteros válidos.")

    tk.Button(win, text="Calcular con repeticion", command=calcular2, bg="#3498db", fg="white").pack(pady=10)
