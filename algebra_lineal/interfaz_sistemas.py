import tkinter as tk
from tkinter import messagebox, scrolledtext
import numpy as np
from utilidades import crear_ventana_base, leer_matriz_gui
from logica import gauss_jordan, regla_cramer

def ventana_sistemas():
    """Ventana para resolver sistemas de ecuaciones"""
    ventana = crear_ventana_base("Sistemas de Ecuaciones", 700, 700)
    
    # Configuración
    frame_config = tk.Frame(ventana, bg="#f0f0f0")
    frame_config.pack(pady=10)
    
    tk.Label(frame_config, text="Tamaño del sistema:", font=('Arial', 11), bg="#f0f0f0").grid(row=0, column=0, padx=5)
    tamaño_var = tk.StringVar(value="2")
    combo = tk.Spinbox(frame_config, from_=2, to=4, textvariable=tamaño_var, width=5)
    combo.grid(row=0, column=1, padx=5)
    
    tk.Label(frame_config, text="Método:", font=('Arial', 11), bg="#f0f0f0").grid(row=0, column=2, padx=5)
    metodo_var = tk.StringVar(value="gauss")
    tk.Radiobutton(frame_config, text="Gauss-Jordan", variable=metodo_var, value="gauss", bg="#f0f0f0").grid(row=0, column=3)
    tk.Radiobutton(frame_config, text="Cramer", variable=metodo_var, value="cramer", bg="#f0f0f0").grid(row=0, column=4)
    
    # Frame para matriz y vector
    frame_sistema = tk.Frame(ventana, bg="white", relief=tk.RIDGE, bd=2)
    frame_sistema.pack(pady=10)
    
    entradas_A = []
    entradas_b = []
    
    def crear_sistema():
        """Crea el sistema de ecuaciones"""
        for widget in frame_sistema.winfo_children():
            widget.destroy()
        
        n = int(tamaño_var.get())
        
        tk.Label(frame_sistema, text=f"Sistema de Ecuaciones {n}x{n}", 
                font=('Arial', 11, 'bold'), bg="white").grid(row=0, column=0, columnspan=n+2, pady=10)
        
        tk.Label(frame_sistema, text="Coeficientes (A)", font=('Arial', 9, 'bold'), bg="white").grid(row=1, column=0, columnspan=n)
        tk.Label(frame_sistema, text="=", font=('Arial', 10, 'bold'), bg="white").grid(row=1, column=n)
        tk.Label(frame_sistema, text="Términos (b)", font=('Arial', 9, 'bold'), bg="white").grid(row=1, column=n+1)
        
        entradas_A.clear()
        entradas_b.clear()
        
        for i in range(n):
            fila = []
            for j in range(n):
                entrada = tk.Entry(frame_sistema, width=7, justify='center')
                entrada.grid(row=i+2, column=j, padx=3, pady=3)
                entrada.insert(0, "0")
                fila.append(entrada)
            entradas_A.append(fila)
            
            entrada_b = tk.Entry(frame_sistema, width=7, justify='center')
            entrada_b.grid(row=i+2, column=n+1, padx=3, pady=3)
            entrada_b.insert(0, "0")
            entradas_b.append(entrada_b)
    
    def resolver():
        """Resuelve el sistema"""
        A = leer_matriz_gui(entradas_A)
        if A is None:
            return
        
        try:
            b = np.array([float(e.get()) for e in entradas_b])
        except ValueError:
            messagebox.showerror("Error", "Valores inválidos en términos independientes")
            return
        
        resultado = "SISTEMA DE ECUACIONES\n" + "="*50 + "\n"
        
        # Mostrar ecuaciones
        for i in range(len(b)):
            ec = " + ".join([f"({round(A[i][j], 2)})x{j+1}" for j in range(len(b))])
            ec = ec.replace("+ -", "- ")
            resultado += f"  {ec} = {round(b[i], 2)}\n"
        
        # Resolver
        if metodo_var.get() == "gauss":
            sol, tipo, texto = gauss_jordan(A, b)
        else:
            sol, tipo, texto = regla_cramer(A, b)
        
        resultado += texto
        
        # Resultado final
        resultado += "\n" + "="*50 + "\n"
        resultado += "RESULTADO FINAL:\n" + "="*50 + "\n"
        
        if tipo == "única":
            resultado += " SOLUCIÓN ÚNICA:\n"
            for i, s in enumerate(sol):
                resultado += f"  x{i+1} = {round(s, 4)}\n"
        elif tipo == "sin solución":
            resultado += " SIN SOLUCIÓN (sistema inconsistente)\n"
        elif tipo == "infinitas":
            resultado += " INFINITAS SOLUCIONES (sistema dependiente)\n"
        
        texto_resultado.delete(1.0, tk.END)
        texto_resultado.insert(1.0, resultado)
    
    btn_crear = tk.Button(frame_config, text="Crear Sistema", command=crear_sistema,
                         bg="#4CAF50", fg="white", font=('Arial', 10, 'bold'))
    btn_crear.grid(row=1, column=0, columnspan=5, pady=10)
    
    # Botones
    frame_botones = tk.Frame(ventana, bg="#f0f0f0")
    frame_botones.pack(pady=10)
    
    btn_resolver = tk.Button(frame_botones, text="Resolver Sistema", command=resolver,
                            bg="#2196F3", fg="white", font=('Arial', 11, 'bold'), padx=20, pady=5)
    btn_resolver.pack(side=tk.LEFT, padx=5)
    
    btn_cerrar = tk.Button(frame_botones, text="Cerrar", command=ventana.destroy,
                          bg="#f44336", fg="white", font=('Arial', 11, 'bold'), padx=20, pady=5)
    btn_cerrar.pack(side=tk.LEFT, padx=5)
    
    # Resultados
    tk.Label(ventana, text="Proceso y Resultados:", font=('Arial', 11, 'bold'), bg="#f0f0f0").pack()
    texto_resultado = scrolledtext.ScrolledText(ventana, width=70, height=20, font=('Courier', 8))
    texto_resultado.pack(pady=5, padx=10)
    
    crear_sistema()