import tkinter as tk
from tkinter import scrolledtext
import numpy as np
from utilidades import crear_ventana_base, leer_matriz_gui, mostrar_matriz_texto

def ventana_inversa():
    """Ventana para calcular la inversa de una matriz"""
    ventana = crear_ventana_base("Inversa de Matriz", 700, 600)
    
    # Frame superior para configuración
    frame_config = tk.Frame(ventana, bg="#f0f0f0")
    frame_config.pack(pady=10)
    
    tk.Label(frame_config, text="Tamaño de la matriz:", font=('Arial', 11), bg="#f0f0f0").pack(side=tk.LEFT, padx=5)
    
    tamaño_var = tk.StringVar(value="2")
    combo = tk.Spinbox(frame_config, from_=2, to=5, textvariable=tamaño_var, width=5, font=('Arial', 11))
    combo.pack(side=tk.LEFT, padx=5)
    
    # Frame para la matriz
    frame_matriz = tk.Frame(ventana, bg="white", relief=tk.RIDGE, bd=2)
    frame_matriz.pack(pady=10)
    
    entradas = []
    
    def crear_matriz():
        """Crea la cuadrícula de entrada"""
        for widget in frame_matriz.winfo_children():
            widget.destroy()
        
        n = int(tamaño_var.get())
        tk.Label(frame_matriz, text=f"Ingrese los elementos de la matriz {n}×{n}:", 
                font=('Arial', 11, 'bold'), bg="white").grid(row=0, column=0, columnspan=n, pady=10)
        
        entradas.clear()
        for i in range(n):
            fila_entradas = []
            for j in range(n):
                entrada = tk.Entry(frame_matriz, width=8, justify='center', font=('Arial', 10))
                entrada.grid(row=i+1, column=j, padx=5, pady=5)
                entrada.insert(0, "0")
                fila_entradas.append(entrada)
            entradas.append(fila_entradas)
    
    def calcular():
        """Calcula la inversa"""
        A = leer_matriz_gui(entradas)
        if A is None:
            return
        
        # Calcular determinante
        det = np.linalg.det(A)
        
        resultado = f"MATRIZ ORIGINAL:\n"
        resultado += mostrar_matriz_texto(A, "A")
        resultado += f"\nDeterminante: {round(det, 4)}\n\n"
        
        if abs(det) < 1e-10:
            resultado += "Esta matriz NO tiene inversa (determinante = 0)\n"
            resultado += "Una matriz solo tiene inversa si su determinante es diferente de cero."
        else:
            A_inv = np.linalg.inv(A)
            resultado += "La matriz SÍ tiene inversa\n\n"
            resultado += mostrar_matriz_texto(A_inv, "MATRIZ INVERSA (A⁻¹)")
            
            # Verificación
            verificacion = np.dot(A, A_inv)
            resultado += "\nVERIFICACIÓN (A × A⁻¹ debe ser la matriz identidad):\n"
            resultado += mostrar_matriz_texto(verificacion, "A × A⁻¹")
        
        texto_resultado.delete(1.0, tk.END)
        texto_resultado.insert(1.0, resultado)
    
    # Botón para crear/actualizar matriz
    btn_crear = tk.Button(frame_config, text="Crear Matriz", command=crear_matriz, 
                         bg="#4CAF50", fg="white", font=('Arial', 10, 'bold'), padx=10)
    btn_crear.pack(side=tk.LEFT, padx=5)
    
    # Botones
    frame_botones = tk.Frame(ventana, bg="#f0f0f0")
    frame_botones.pack(pady=10)
    
    btn_calcular = tk.Button(frame_botones, text="Calcular Inversa", command=calcular,
                            bg="#2196F3", fg="white", font=('Arial', 11, 'bold'), padx=20, pady=5)
    btn_calcular.pack(side=tk.LEFT, padx=5)
    
    btn_cerrar = tk.Button(frame_botones, text="Cerrar", command=ventana.destroy,
                          bg="#f44336", fg="white", font=('Arial', 11, 'bold'), padx=20, pady=5)
    btn_cerrar.pack(side=tk.LEFT, padx=5)
    
    # Área de resultados
    tk.Label(ventana, text="Resultados:", font=('Arial', 11, 'bold'), bg="#f0f0f0").pack()
    texto_resultado = scrolledtext.ScrolledText(ventana, width=70, height=15, font=('Courier', 9))
    texto_resultado.pack(pady=5, padx=10)
    
    # Crear matriz inicial
    crear_matriz()