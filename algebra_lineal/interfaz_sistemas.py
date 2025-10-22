import tkinter as tk
from tkinter import messagebox, scrolledtext
import numpy as np
from utilidades import crear_ventana_base, leer_matriz_gui, mostrar_matriz_texto

def gauss_jordan_texto(A, b):
    """Resuelve por Gauss-Jordan y retorna texto del proceso"""
    n = len(b)
    Ab = np.column_stack([A.copy(), b.copy()])
    
    texto = "\n--- MÉTODO DE GAUSS-JORDAN ---\n\n"
    texto += "MATRIZ AUMENTADA INICIAL [A|b]:\n"
    texto += mostrar_matriz_texto(Ab)
    
    for i in range(n):
        max_fila = i
        for k in range(i + 1, n):
            if abs(Ab[k][i]) > abs(Ab[max_fila][i]):
                max_fila = k
        
        if max_fila != i:
            Ab[[i, max_fila]] = Ab[[max_fila, i]]
            texto += f"Intercambio filas {i+1} ↔ {max_fila+1}\n"
        
        if abs(Ab[i][i]) < 1e-10:
            continue
        
        Ab[i] = Ab[i] / Ab[i][i]
        texto += f"\nPaso {i+1}: Hacer pivote = 1 en fila {i+1}\n"
        texto += mostrar_matriz_texto(Ab)
        
        for k in range(n):
            if k != i and abs(Ab[k][i]) > 1e-10:
                Ab[k] = Ab[k] - Ab[k][i] * Ab[i]
    
    return analizar_solucion_texto(Ab, n, texto)

def regla_cramer_texto(A, b):
    """Resuelve por Cramer y retorna texto"""
    texto = "\n--- REGLA DE CRAMER ---\n\n"
    det_A = np.linalg.det(A)
    texto += f"Determinante de A: {round(det_A, 4)}\n\n"
    
    if abs(det_A) < 1e-10:
        texto += " Determinante = 0, no se puede usar Cramer\n"
        return None, "indeterminado", texto
    
    n = len(b)
    soluciones = []
    
    for i in range(n):
        A_i = A.copy()
        A_i[:, i] = b
        det_i = np.linalg.det(A_i)
        sol = det_i / det_A
        texto += f"x{i+1}: Det(A{i+1}) = {round(det_i, 4)} → x{i+1} = {round(sol, 4)}\n"
        soluciones.append(sol)
    
    return soluciones, "única", texto

def analizar_solucion_texto(Ab, n, texto_previo):
    """Analiza solución y retorna resultado"""
    A_red = Ab[:, :-1]
    b_red = Ab[:, -1]
    
    rango_A = np.linalg.matrix_rank(A_red)
    rango_Ab = np.linalg.matrix_rank(Ab)
    
    texto_previo += f"\n--- ANÁLISIS ---\n"
    texto_previo += f"Rango(A) = {rango_A}\n"
    texto_previo += f"Rango([A|b]) = {rango_Ab}\n"
    texto_previo += f"Variables = {n}\n\n"
    
    if rango_A < rango_Ab:
        return None, "sin solución", texto_previo
    elif rango_A == rango_Ab == n:
        return b_red[:n].tolist(), "única", texto_previo
    else:
        return None, "infinitas", texto_previo

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
        
        tk.Label(frame_sistema, text=f"Sistema de Ecuaciones {n}×{n}", 
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
        resultado += mostrar_matriz_texto(A, "Matriz A")
        resultado += f"Vector b: {[round(x, 4) for x in b]}\n"
        
        # Mostrar ecuaciones
        resultado += "\nEcuaciones:\n"
        for i in range(len(b)):
            ec = " + ".join([f"({round(A[i][j], 2)})x{j+1}" for j in range(len(b))])
            ec = ec.replace("+ -", "- ")
            resultado += f"  {ec} = {round(b[i], 2)}\n"
        
        # Resolver
        if metodo_var.get() == "gauss":
            sol, tipo, texto = gauss_jordan_texto(A, b)
        else:
            sol, tipo, texto = regla_cramer_texto(A, b)
        
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