import tkinter as tk
from tkinter import messagebox
from logica import calcular_permutacion_sin_repeticion, calcular_permutacion_con_repeticion

def ventana_permutaciones():
    win = tk.Toplevel()
    win.title("Permutaciones")
    win.geometry("300x300")
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
            res = calcular_permutacion_sin_repeticion(n, r)
            resultado.config(text=f"Permutaciones sin Repeticion: {res}")
        except:
            messagebox.showerror("Error", "Ingresa valores enteros válidos.")

    tk.Button(win, text="Calcular Permutacion sin repeticion", command=calcular1, bg="#595fb6", fg="white", width=30, height=2, font=('Arial', 10)).pack(pady=5)

    def calcular2():
        try:
            n = int(entry_n.get())
            r = int(entry_r.get())
            res = calcular_permutacion_con_repeticion(n, r)
            resultado.config(text=f"Permutaciones con Repeticion: {res}")
        except:
            messagebox.showerror("Error", "Ingresa valores enteros válidos.")

    tk.Button(win, text="Calcular Permutacion con repeticion", command=calcular2, bg="#9b59b6", fg="white", width=30, height=2, font=('Arial', 10)).pack(pady=5)