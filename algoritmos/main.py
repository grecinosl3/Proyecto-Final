import tkinter as tk
from interfaz_inventario import ventana_productos
from interfaz_clientes import interfaz_clientes 
from interfaz_ventas import ventana_ventas
from interfaz_reportes import ventana_reportes

def main():
    """Ventana Principal del Proyecto de Algoritmos"""
    root = tk.Tk()
    root.title("Proyecto de Algoritmos")
    root.geometry("500x600")
    root.configure(bg="#2c3e50")

    # Título
    frame_titulo = tk.Frame(root, bg="#34495e", pady=20)
    frame_titulo.pack(fill=tk.X)

    tk.Label(frame_titulo, text="PROYECTO DE", font=('Arial', 14), 
             bg="#34495e", fg="white").pack()
    tk.Label(frame_titulo, text="ALGORITMOS", font=('Arial', 24, 'bold'), 
             bg="#34495e", fg="#f39c12").pack()
    tk.Label(frame_titulo, text="Control de Inventario, Clientes, Ventas y Reportes", 
             font=('Arial', 10), bg="#34495e", fg="#ecf0f1").pack()

    # Frame de botones
    frame_botones = tk.Frame(root, bg="#2c3e50", pady=30)
    frame_botones.pack(expand=True)

    # Botones
    btn_inventario = tk.Button(frame_botones, text=" Control de Inventario", 
                               command=ventana_productos,
                               bg="#3498db", fg="white", font=('Arial', 13, 'bold'),
                               width=30, height=2, cursor="hand2")
    btn_inventario.pack(pady=10)

    btn_clientes = tk.Button(frame_botones, text=" Control de Clientes", 
                             command=interfaz_clientes,
                             bg="#27ae60", fg="white", font=('Arial', 13, 'bold'),
                             width=30, height=2, cursor="hand2")
    btn_clientes.pack(pady=10)

    btn_ventas = tk.Button(frame_botones, text=" Control de Ventas", 
                           command=ventana_ventas,
                           bg="#9b59b6", fg="white", font=('Arial', 13, 'bold'),
                           width=30, height=2, cursor="hand2")
    btn_ventas.pack(pady=10)
    
    btn_reportes = tk.Button(frame_botones, text=" Reportes", command=ventana_reportes,
                         bg="#e67e22", fg="white", font=('Arial', 13, 'bold'),
                         width=30, height=2, cursor="hand2")
    btn_reportes.pack(pady=10)

    btn_salir = tk.Button(frame_botones, text=" Salir", 
                          command=root.quit,
                          bg="#95a5a6", fg="white", font=('Arial', 11),
                          width=15, cursor="hand2")
    btn_salir.pack(pady=20)

    # Footer
    tk.Label(root, text="Desarrollado con Python + Tkinter", 
             font=('Arial', 8), bg="#2c3e50", fg="#7f8c8d").pack(side=tk.BOTTOM, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
