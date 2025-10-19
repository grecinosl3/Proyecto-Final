# ventas_gui.py

import tkinter as tk
from tkinter import messagebox, ttk
from ventas import listar_ventas, crear_venta, anular_venta

def ventana_ventas():
    win = tk.Toplevel()
    win.title("Gestión de Ventas")
    win.geometry("700x500")
    win.configure(bg="#ecf0f1")

    # Frame para lista de ventas
    frame_lista = tk.Frame(win)
    frame_lista.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    columnas = ("codigo_producto", "codigo_cliente", "cantidad_producto", "total_ventas")
    tree = ttk.Treeview(frame_lista, columns=columnas, show="headings")

    for col in columnas:
        tree.heading(col, text=col.replace("_", " ").title())
        tree.column(col, width=150)

    tree.pack(fill=tk.BOTH, expand=True)

    def cargar_ventas():
        for fila in tree.get_children():
            tree.delete(fila)
        ventas = listar_ventas()
        for v in ventas:
            tree.insert("", tk.END, values=(v["codigo producto"], v["codigo cliente"], v["cantidad producto"], v["total ventas"]))

    cargar_ventas()

    # Frame para formulario creación
    frame_form = tk.Frame(win, bg="#ecf0f1")
    frame_form.pack(fill=tk.X, padx=10)

    tk.Label(frame_form, text="Código Producto:", bg="#ecf0f1").grid(row=0, column=0, sticky="e", pady=2)
    entrada_codigo_prod = tk.Entry(frame_form)
    entrada_codigo_prod.grid(row=0, column=1, pady=2)

    tk.Label(frame_form, text="Código Cliente:", bg="#ecf0f1").grid(row=1, column=0, sticky="e", pady=2)
    entrada_codigo_cli = tk.Entry(frame_form)
    entrada_codigo_cli.grid(row=1, column=1, pady=2)

    tk.Label(frame_form, text="Cantidad:", bg="#ecf0f1").grid(row=2, column=0, sticky="e", pady=2)
    entrada_cantidad = tk.Entry(frame_form)
    entrada_cantidad.grid(row=2, column=1, pady=2)

    tk.Label(frame_form, text="Total Ventas:", bg="#ecf0f1").grid(row=3, column=0, sticky="e", pady=2)
    entrada_total = tk.Entry(frame_form)
    entrada_total.grid(row=3, column=1, pady=2)

    def agregar_venta():
        try:
            codigo_prod = entrada_codigo_prod.get().strip()
            codigo_cli = entrada_codigo_cli.get().strip()
            cantidad = int(entrada_cantidad.get())
            total = float(entrada_total.get())
            if not codigo_prod or not codigo_cli:
                messagebox.showerror("Error", "Código producto y cliente no pueden estar vacíos.")
                return
            crear_venta(codigo_prod, codigo_cli, cantidad, total)
            messagebox.showinfo("Éxito", "Venta agregada correctamente.")
            cargar_ventas()
            entrada_codigo_prod.delete(0, tk.END)
            entrada_codigo_cli.delete(0, tk.END)
            entrada_cantidad.delete(0, tk.END)
            entrada_total.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Cantidad y total deben ser numéricos.")

    btn_agregar = tk.Button(frame_form, text="Agregar Venta", command=agregar_venta, bg="#3498db", fg="white")
    btn_agregar.grid(row=4, column=0, columnspan=2, pady=10)

    # Frame para anular venta
    frame_anular = tk.Frame(win, bg="#ecf0f1")
    frame_anular.pack(fill=tk.X, padx=10, pady=10)

    tk.Label(frame_anular, text="Código producto a anular:", bg="#ecf0f1").grid(row=0, column=0)
    entrada_anular = tk.Entry(frame_anular)
    entrada_anular.grid(row=0, column=1)

    def anular():
        codigo = entrada_anular.get().strip()
        if not codigo:
            messagebox.showerror("Error", "Ingresá un código válido.")
            return
        eliminado = anular_venta(codigo)
        if eliminado:
            messagebox.showinfo("Éxito", f"Venta con código {codigo} eliminada.")
            cargar_ventas()
            entrada_anular.delete(0, tk.END)
        else:
            messagebox.showwarning("No encontrado", "No se encontró la venta con ese código.")

    btn_anular = tk.Button(frame_anular, text="Anular Venta", command=anular, bg="#e74c3c", fg="white")
    btn_anular.grid(row=1, column=0, columnspan=2, pady=5)