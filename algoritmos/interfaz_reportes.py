import tkinter as tk
from tkinter import ttk
from reportes import ventas_por_cliente, ventas_por_producto

def ventana_reportes():
    win = tk.Toplevel()
    win.title("Reportes")
    win.geometry("600x400")
    win.configure(bg="#2c3e50")

    # Frame para botones de reporte
    frame_botones = tk.Frame(win, bg="#2c3e50", pady=30)
    frame_botones.pack(expand=True)

    btn_cliente = tk.Button(frame_botones, text="Ventas por Cliente",
                           command=lambda: mostrar_reporte(ventas_por_cliente(), ["Código Cliente", "Nombre Cliente", "Total Ventas"], "Ventas por Cliente"),
                           bg="#2980b9", fg="white", font=('Arial', 13, 'bold'),
                           width=30, height=2, cursor="hand2")
    btn_cliente.pack(pady=10)

    btn_producto = tk.Button(frame_botones, text="Ventas por Producto",
                            command=lambda: mostrar_reporte(ventas_por_producto(), ["Código Producto", "Nombre Producto", "Cantidad Vendida"], "Ventas por Producto"),
                            bg="#27ae60", fg="white", font=('Arial', 13, 'bold'),
                            width=30, height=2, cursor="hand2")
    btn_producto.pack(pady=10)

    def mostrar_reporte(data, columnas, titulo):
        top = tk.Toplevel(win)
        top.title(titulo)
        tree = ttk.Treeview(top, columns=columnas, show="headings")
        for col in columnas:
            tree.heading(col, text=col)
            tree.column(col, width=180)
        tree.pack(fill=tk.BOTH, expand=True)

        for fila in data:
            tree.insert("", tk.END, values=fila)

