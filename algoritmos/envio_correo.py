import tkinter as tk
from tkinter import messagebox
import os
from reportes import guardar_reporte_ventas_por_cliente, guardar_reporte_ventas_por_producto
from enviar_con_adjunto import enviar_mensaje


def guardar_y_enviar_reporte(destinatario_email):
    nombre_archivo = "ventas_por_cliente.xlsx"
    ruta_archivo = os.path.abspath(nombre_archivo)

    guardar_reporte_ventas_por_cliente(nombre_archivo)

    asunto = "Reporte de Ventas por Cliente"
    cuerpo = "Adjunto encontrarás el reporte actualizado de ventas por cliente."
    titulo = "Reporte Ventas por Cliente"
    ruta_de_adjunto = os.path.dirname(ruta_archivo)

    try:
        enviar_mensaje(
            asunto=asunto,
            cuerpo=cuerpo,
            destinatario=destinatario_email,
            titulo=titulo,
            nombre_archivo=nombre_archivo,
            ruta_de_adjunto=ruta_de_adjunto
        )
        messagebox.showinfo("Éxito", "Reporte guardado y correo enviado correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo enviar el correo:\n{e}")

#ENVIAR POR PRODUCTO

def guardar_y_enviar_reporte_producto(destinatario_email):
    nombre_archivo = "ventas_por_producto.xlsx"
    ruta_archivo = os.path.abspath(nombre_archivo)

    guardar_reporte_ventas_por_producto(nombre_archivo)

    asunto = "Reporte de Ventas por Producto"
    cuerpo = "Adjunto encontrarás el reporte actualizado de ventas por producto."
    titulo = "Reporte Ventas por Producto"
    ruta_de_adjunto = os.path.dirname(ruta_archivo)

    try:
        enviar_mensaje(
            asunto=asunto,
            cuerpo=cuerpo,
            destinatario=destinatario_email,
            titulo=titulo,
            nombre_archivo=nombre_archivo,
            ruta_de_adjunto=ruta_de_adjunto
        )
        messagebox.showinfo("Éxito", "Reporte guardado y correo enviado correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo enviar el correo:\n{e}")
