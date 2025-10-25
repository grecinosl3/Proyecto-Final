import tkinter as tk
from tkinter import ttk
from reportes import ventas_por_cliente, ventas_por_producto
from envio_correo import guardar_y_enviar_reporte, guardar_y_enviar_reporte_producto
import tkinter as tk
from tkinter import simpledialog


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
                            command=lambda: mostrar_reporte(ventas_por_producto(), ["Código Producto", "Nombre Producto", "Cantidad Total", "Total_Ventas"], "Ventas por Producto"),
                            bg="#27ae60", fg="white", font=('Arial', 13, 'bold'),
                            width=30, height=2, cursor="hand2")
    btn_producto.pack(pady=10)

    # Botón para guardar y enviar correo
    def pedir_email_y_enviar():
        email = simpledialog.askstring("Enviar reporte", "Ingresa el email del destinatario:")
        if email:
            guardar_y_enviar_reporte(email)

    btn_enviar_reporte = tk.Button(frame_botones, text="Guardar y Enviar Reporte por Email",
                                  command=pedir_email_y_enviar,
                                  bg="#f39c12", fg="white", font=('Arial', 12, 'bold'),
                                  width=30, height=2, cursor="hand2")
    btn_enviar_reporte.pack(pady=10)

    def pedir_email_y_enviar_producto():
        email = simpledialog.askstring("Enviar reporte", "Ingresa el email del destinatario:")
        if email:
            guardar_y_enviar_reporte_producto(email)

    btn_enviar_reporte_producto = tk.Button(frame_botones, text="Guardar y Enviar Reporte Producto por Email",
                                        command=pedir_email_y_enviar_producto,
                                        bg="#e67e22", fg="white", font=('Arial', 12, 'bold'),
                                        width=35, height=2, cursor="hand2")
    btn_enviar_reporte_producto.pack(pady=10)

#Muestra los reportes en cada parametro
    def mostrar_reporte(data, columnas, titulo):
        top = tk.Toplevel(win)
        top.title(titulo)
        
        #Crea el treeview con las columnas
        tree = ttk.Treeview(top, columns=columnas, show="headings")
        for col in columnas:
            tree.heading(col, text=col)
            tree.column(col, width=250)
        tree.pack(fill=tk.BOTH, expand=True)

        #Inserta datos en la pantalla blanca(Treeview)
        for fila in data:
            tree.insert("", tk.END, values=fila)
