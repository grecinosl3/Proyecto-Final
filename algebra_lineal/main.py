import tkinter as tk
from interfaz_inversa import ventana_inversa
from interfaz_multiplicacion import ventana_multiplicacion
from interfaz_sistemas import ventana_sistemas

def main():
    """Ventana principal"""
    root = tk.Tk()
    root.title("Proyecto de Álgebra Lineal")
    root.geometry("500x550")
    root.configure(bg="#2c3e50")
    
    # Título
    frame_titulo = tk.Frame(root, bg="#34495e", pady=20)
    frame_titulo.pack(fill=tk.X)
    
    tk.Label(frame_titulo, text="PROYECTO DE", font=('Arial', 14), 
            bg="#34495e", fg="white").pack()
    tk.Label(frame_titulo, text="ÁLGEBRA LINEAL", font=('Arial', 24, 'bold'), 
            bg="#34495e", fg="#3498db").pack()
    tk.Label(frame_titulo, text="Operaciones con Matrices y Sistemas", 
            font=('Arial', 10), bg="#34495e", fg="#ecf0f1").pack()
    
    # Frame de botones
    frame_botones = tk.Frame(root, bg="#2c3e50", pady=30)
    frame_botones.pack(expand=True)
    
    # Botones principales
    btn_inversa = tk.Button(frame_botones, text=" Inversa de Matriz", 
                           command=ventana_inversa,
                           bg="#3498db", fg="white", font=('Arial', 13, 'bold'),
                           width=30, height=2, cursor="hand2")
    btn_inversa.pack(pady=10)
    
    btn_mult = tk.Button(frame_botones, text=" Multiplicación de Matrices", 
                        command=ventana_multiplicacion,
                        bg="#9b59b6", fg="white", font=('Arial', 13, 'bold'),
                        width=30, height=2, cursor="hand2")
    btn_mult.pack(pady=10)
    
    btn_sistemas = tk.Button(frame_botones, text=" Sistemas de Ecuaciones", 
                            command=ventana_sistemas,
                            bg="#e74c3c", fg="white", font=('Arial', 13, 'bold'),
                            width=30, height=2, cursor="hand2")
    btn_sistemas.pack(pady=10)
    
    btn_salir = tk.Button(frame_botones, text=" Salir", 
                         command=root.quit,
                         bg="#95a5a6", fg="white", font=('Arial', 11),
                         width=15, cursor="hand2")
    btn_salir.pack(pady=20)
    
    # Footer
    tk.Label(root, text="Desarrollado con Python + Tkinter + NumPy", 
            font=('Arial', 8), bg="#2c3e50", fg="#7f8c8d").pack(side=tk.BOTTOM, pady=30)
    
    root.mainloop()

if __name__ == "__main__":
    main()