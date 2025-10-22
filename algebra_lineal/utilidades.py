import numpy as np
import tkinter as tk
from tkinter import messagebox
from fractions import Fraction

def crear_ventana_base(titulo, ancho=600, alto=500):
    """Crea una ventana base para la aplicación"""
    ventana = tk.Toplevel()
    ventana.title(titulo)
    ventana.geometry(f"{ancho}x{alto}")
    ventana.configure(bg="#f0f0f0")
    return ventana

def crear_entrada_matriz(frame, filas, columnas):
    """Crea una cuadrícula de entradas para una matriz"""
    entradas = []
    for i in range(filas):
        fila_entradas = []
        for j in range(columnas):
            entrada = tk.Entry(frame, width=8, justify='center', font=('Arial', 10))
            entrada.grid(row=i, column=j, padx=5, pady=5)
            fila_entradas.append(entrada)
        entradas.append(fila_entradas)
    return entradas

def leer_matriz_gui(entradas):
    """Lee los valores de las entradas de matriz"""
    try:
        matriz = []
        for fila in entradas:
            fila_valores = []
            for entrada in fila:
                valor = entrada.get().strip()
                if valor == "":
                    valor = "0"
                fila_valores.append(float(valor))
            matriz.append(fila_valores)
        return np.array(matriz)
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese solo números válidos")
        return None

def mostrar_matriz_texto(matriz, nombre="Matriz"):
    """Convierte una matriz a texto formateado"""
    texto = f"{nombre}:\n"
    for fila in matriz:
        fila_frac = [Fraction(float(x)).limit_denominator(1000) for x in fila]
        texto += "[" + " ".join(str(f) for f in fila_frac) + "]\n"  
    return texto + "\n"