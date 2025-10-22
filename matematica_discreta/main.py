import tkinter as tk
from interfaz_combinaciones import ventana_combinaciones
from interfaz_permutaciones import ventana_permutaciones
from interfaz_conjuntos import ventana_conjuntos
from interfaz_cmd import ventana_mcd

def main():
    """Ventana principal"""
    root = tk.Tk()
    root.title("Proyecto de Matemática Discreta")
    root.geometry("500x500")
    root.configure(bg="#2c3e50")
    
    # Título
    frame_titulo = tk.Frame(root, bg="#34495e", pady=20)
    frame_titulo.pack(fill=tk.X)
    
    tk.Label(frame_titulo, text="PROYECTO DE", font=('Arial', 14), 
             bg="#34495e", fg="white").pack()
    tk.Label(frame_titulo, text="MATEMÁTICA DISCRETA", font=('Arial', 24, 'bold'), 
             bg="#34495e", fg="#3498db").pack()
    tk.Label(frame_titulo, text="Combinaciones, Permutaciones, Conjuntos y CMD", 
             font=('Arial', 10), bg="#34495e", fg="#ecf0f1").pack()
    
    # Frame de botones
    frame_botones = tk.Frame(root, bg="#2c3e50", pady=30)
    frame_botones.pack(expand=True)
    
    # Botones principales
    btn_comb = tk.Button(frame_botones, text=" Combinaciones", 
                         command=ventana_combinaciones,
                         bg="#3498db", fg="white", font=('Arial', 13, 'bold'),
                         width=30, height=2, cursor="hand2")
    btn_comb.pack(pady=5)
    
    btn_perm = tk.Button(frame_botones, text=" Permutaciones", 
                         command=ventana_permutaciones,
                         bg="#9b59b6", fg="white", font=('Arial', 13, 'bold'),
                         width=30, height=2, cursor="hand2")
    btn_perm.pack(pady=5)
    
    btn_conj = tk.Button(frame_botones, text=" Operaciones con Conjuntos", 
                         command=ventana_conjuntos,
                         bg="#e67e22", fg="white", font=('Arial', 13, 'bold'),
                         width=30, height=2, cursor="hand2")
    btn_conj.pack(pady=5)

    btn_conj = tk.Button(frame_botones, text=" MCD ", command=ventana_mcd,
                         bg="#424cdb", fg="white", font=('Arial', 13, 'bold'),
                         width=30, height=2, cursor="hand2")
    btn_conj.pack(pady=5)

    btn_salir = tk.Button(frame_botones, text=" Salir", 
                          command=root.quit,
                          bg="#95a5a6", fg="white", font=('Arial', 11),
                          width=15, cursor="hand2")
    btn_salir.pack(pady=10)
    
    # Footer
    tk.Label(root, text="Desarrollado con Python + Tkinter", 
             font=('Arial', 8), bg="#2c3e50", fg="#7f8c8d").pack(side=tk.BOTTOM, pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    main()
