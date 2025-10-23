import tkinter as tk
from tkinter import scrolledtext
from utilidades import crear_ventana_base, leer_matriz_gui
from logica import multiplicar_matrices

def ventana_multiplicacion():
    """Ventana para multiplicar matrices"""
    ventana = crear_ventana_base("Multiplicación de Matrices", 800, 650)
    
    # Frame de configuración
    frame_config = tk.Frame(ventana, bg="#f0f0f0")
    frame_config.pack(pady=10)
    
    # Primera matriz
    tk.Label(frame_config, text="Matriz A:", font=('Arial', 11, 'bold'), bg="#f0f0f0").grid(row=0, column=0, columnspan=2, pady=5)
    tk.Label(frame_config, text="Filas:", bg="#f0f0f0").grid(row=1, column=0, padx=5)
    filas1_var = tk.Spinbox(frame_config, from_=2, to=3, width=5)
    filas1_var.grid(row=1, column=1, padx=5)
    filas1_var.delete(0, tk.END)
    filas1_var.insert(0, "2")
    
    tk.Label(frame_config, text="Columnas:", bg="#f0f0f0").grid(row=2, column=0, padx=5)
    cols1_var = tk.Spinbox(frame_config, from_=2, to=3, width=5)
    cols1_var.grid(row=2, column=1, padx=5)
    cols1_var.delete(0, tk.END)
    cols1_var.insert(0, "2")
    
    # Segunda matriz
    tk.Label(frame_config, text="Matriz B:", font=('Arial', 11, 'bold'), bg="#f0f0f0").grid(row=0, column=3, columnspan=2, pady=5)
    tk.Label(frame_config, text="Filas:", bg="#f0f0f0").grid(row=1, column=3, padx=5)
    filas2_var = tk.Spinbox(frame_config, from_=2, to=3, width=5)
    filas2_var.grid(row=1, column=4, padx=5)
    filas2_var.delete(0, tk.END)
    filas2_var.insert(0, "2")
    
    tk.Label(frame_config, text="Columnas:", bg="#f0f0f0").grid(row=2, column=3, padx=5)
    cols2_var = tk.Spinbox(frame_config, from_=2, to=3, width=5)
    cols2_var.grid(row=2, column=4, padx=5)
    cols2_var.delete(0, tk.END)
    cols2_var.insert(0, "2")
    
    # Frame para matrices
    frame_matrices = tk.Frame(ventana, bg="#f0f0f0")
    frame_matrices.pack(pady=10)
    
    frame_matriz1 = tk.Frame(frame_matrices, bg="white", relief=tk.RIDGE, bd=2)
    frame_matriz1.pack(side=tk.LEFT, padx=10)
    
    frame_matriz2 = tk.Frame(frame_matrices, bg="white", relief=tk.RIDGE, bd=2)
    frame_matriz2.pack(side=tk.LEFT, padx=10)
    
    entradas1 = []
    entradas2 = []
    
    def crear_matrices():
        """Crea las cuadrículas de entrada"""
        for widget in frame_matriz1.winfo_children():
            widget.destroy()
        for widget in frame_matriz2.winfo_children():
            widget.destroy()
        
        f1, c1 = int(filas1_var.get()), int(cols1_var.get())
        f2, c2 = int(filas2_var.get()), int(cols2_var.get())
        
        # Matriz 1
        tk.Label(frame_matriz1, text=f"Matriz A ({f1}x{c1})", font=('Arial', 10, 'bold'), bg="white").grid(row=0, column=0, columnspan=c1, pady=5)
        entradas1.clear()
        for i in range(f1):
            fila = []
            for j in range(c1):
                entrada = tk.Entry(frame_matriz1, width=7, justify='center', font=('Arial', 9))
                entrada.grid(row=i+1, column=j, padx=3, pady=3)
                entrada.insert(0, "0")
                fila.append(entrada)
            entradas1.append(fila)
        
        # Matriz 2
        tk.Label(frame_matriz2, text=f"Matriz B ({f2}x{c2})", font=('Arial', 10, 'bold'), bg="white").grid(row=0, column=0, columnspan=c2, pady=5)
        entradas2.clear()
        for i in range(f2):
            fila = []
            for j in range(c2):
                entrada = tk.Entry(frame_matriz2, width=7, justify='center', font=('Arial', 9))
                entrada.grid(row=i+1, column=j, padx=3, pady=3)
                entrada.insert(0, "0")
                fila.append(entrada)
            entradas2.append(fila)
    
    def multiplicar():
        """Multiplica las matrices"""
        A = leer_matriz_gui(entradas1)
        B = leer_matriz_gui(entradas2)
        
        if A is None or B is None:
            return
        
        _, texto = multiplicar_matrices(A, B)
        if texto: 
            texto_resultado.delete(1.0, tk.END)
            texto_resultado.insert(1.0, texto)
    
    # Botón crear
    btn_crear = tk.Button(frame_config, text="Crear Matrices", command=crear_matrices,
                         bg="#4CAF50", fg="white", font=('Arial', 10, 'bold'), padx=10)
    
    btn_crear.grid(row=3, column=0, columnspan=5, pady=10)
    
    # Botones
    frame_botones = tk.Frame(ventana, bg="#f0f0f0")
    frame_botones.pack(pady=10)
    
    btn_multiplicar = tk.Button(frame_botones, text="Multiplicar A x B", command=multiplicar,
                               bg="#2196F3", fg="white", font=('Arial', 11, 'bold'), padx=20, pady=5)
    btn_multiplicar.pack(side=tk.LEFT, padx=5)
    
    btn_cerrar = tk.Button(frame_botones, text="Cerrar", command=ventana.destroy,
                          bg="#f44336", fg="white", font=('Arial', 11, 'bold'), padx=20, pady=5)
    btn_cerrar.pack(side=tk.LEFT, padx=5)
    
    # Resultados
    tk.Label(ventana, text="Resultados:", font=('Arial', 11, 'bold'), bg="#f0f0f0").pack()
    texto_resultado = scrolledtext.ScrolledText(ventana, width=80, height=12, font=('Courier', 9))
    texto_resultado.pack(pady=5, padx=10)
    
    crear_matrices()