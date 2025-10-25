import tkinter as tk
from tkinter import messagebox
import sys
import os

class MenuPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Proyecto UMG")
        self.root.geometry("600x550")
        self.root.configure(bg="#1a1a2e")
        self.crear_interfaz()
 
    def crear_interfaz(self):
    # Cargar la imagen y reducir tamaño 
        self.logo_img = tk.PhotoImage(file=os.path.join(os.path.dirname(__file__), "logo.png"))
        self.logo_img = self.logo_img.subsample(3, 3)  

        frame_header = tk.Frame(self.root, bg="#16213e", pady=25)
        frame_header.pack(fill=tk.X)

        frame_contenido = tk.Frame(frame_header, bg="#16213e")
        frame_contenido.pack(anchor="center")

        label_logo = tk.Label(frame_contenido, image=self.logo_img, bg="#16213e")
        label_logo.pack(side=tk.LEFT, padx=10)

        frame_texto = tk.Frame(frame_contenido, bg="#16213e")
        frame_texto.pack(side=tk.LEFT, padx=10)

        tk.Label(frame_texto, text="PROYECTO ",
                 font=('Arial', 16, 'bold'), bg="#16213e", fg="#eaeef1").pack(anchor="center")
        tk.Label(frame_texto, text="Ingeniería En Sistemas",
                 font=('Arial', 28, 'bold'), bg="#16213e", fg="#e94560").pack(pady=5, anchor="center")
        tk.Label(frame_texto, text="Universidad Mariano Galvez -- Ciclo 2025 --",
                 font=('Arial', 11), bg="#16213e", fg="#a8a8a8").pack(anchor="center")  
          
          # Frame contenedor de proyectos
        frame_proyectos = tk.Frame(self.root, bg="#1a1a2e", pady=30)
        frame_proyectos.pack(expand=True)
        
        tk.Label(frame_proyectos, text="Seleccione un Proyecto:", 
                font=('Arial', 14, 'bold'), bg="#1a1a2e", fg="white").pack(pady=2)
        
        # Botón Álgebra Lineal
        btn_algebra = tk.Button(
            frame_proyectos,
            text=" ÁLGEBRA LINEAL",
            command=self.abrir_algebra_lineal,
            bg="#3498db",
            fg="white",
            font=('Arial', 13, 'bold'),
            width=30,
            height=3,
            cursor="hand2",
            relief=tk.RAISED,
            bd=3
        )
        btn_algebra.pack(pady=5)
        
        # Efecto hover
        btn_algebra.bind("<Enter>", lambda e: btn_algebra.config(bg="#2980b9")) #Agregar Hover 
        btn_algebra.bind("<Leave>", lambda e: btn_algebra.config(bg="#3498db"))
        
        # Botón Algoritmos
        btn_algoritmos = tk.Button(
            frame_proyectos,
            text=" ALGORITMOS",
            command=self.abrir_algoritmos,
            bg="#9b59b6",
            fg="white",
            font=('Arial', 13, 'bold'),
            width=30,
            height=3,
            cursor="hand2",
            relief=tk.RAISED,
            bd=3,
        )
        btn_algoritmos.pack(pady=5)
        
        # Botón Matemática Discreta
        btn_discreta = tk.Button(
            frame_proyectos,
            text=" MATEMÁTICA DISCRETA",
            command=self.abrir_matematica_discreta,
            bg="#e74c3c",
            fg="white",
            font=('Arial', 13, 'bold'),
            width=30,
            height=3,
            cursor="hand2",
            relief=tk.RAISED,
            bd=3,
        )
        btn_discreta.pack(pady=5)
        
        # Botón Salir
        frame_footer = tk.Frame(self.root, bg="#1a1a2e", pady=5)
        frame_footer.pack(side=tk.BOTTOM, fill=tk.X)
        
        btn_salir = tk.Button(
            frame_footer,
            text=" Salir",
            command=self.salir,
            bg="#95a5a6",
            fg="white",
            font=('Arial', 11, 'bold'),
            width=10,
            cursor="hand2"
        )
        btn_salir.pack()
        
        # Info
        tk.Label(frame_footer, 
                text="Desarrollado con Python + Tkinter + NumPy + Math | 2025",
                font=('Arial', 8), bg="#1a1a2e", fg="#7f8c8d").pack(pady=3)
    
    def abrir_algebra_lineal(self):
        """Abre el módulo de Álgebra Lineal"""
        try:
            # Importar el módulo de álgebra lineal
            sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'algebra_lineal'))
            from algebra_lineal.main import main as algebra_main
            
            # Crear nueva ventana
            algebra_main()
            
        except ImportError:
            messagebox.showerror(
                "Error", 
                f"No se pudo cargar el módulo de Álgebra Lineal."
            )

    def abrir_algoritmos(self):
        """Abre el módulo de Algoritmos"""
        try:
            sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'algoritmos'))
            from algoritmos.main import main as algoritmos_main
            algoritmos_main()
        except ImportError:
            messagebox.showerror(
                "Error", 
                f"No se pudo cargar el módulo de Algoritmos.")
            
    def abrir_matematica_discreta(self):
        """Abre el módulo de Matemática Discreta"""
        try:
            sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'matematica_discreta'))
            from matematica_discreta.main import main as discreta_main
            discreta_main()
        except ImportError:
            messagebox.showerror(
                "Error", 
                "El módulo de Matemática Discreta aún no está implementado"
            )

    def salir(self):
        """Cierra la aplicación"""
        respuesta = messagebox.askyesno(
            "Salir", 
            "¿Está seguro que desea salir del proyecto?"
        )
        if respuesta:
            self.root.quit()

def main():
    """Función principal"""
    root = tk.Tk()
    app = MenuPrincipal(root)
    root.mainloop()

if __name__ == "__main__":
    main()