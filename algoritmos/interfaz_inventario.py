import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from inventario import listar_productos, crear_producto, actualizar_producto, eliminar_producto, editar_existencia_producto

def ventana_productos():
    win = tk.Toplevel()
    win.title("Gestión de Productos")
    win.geometry("700x400")

    # Frame para la tabla
    frame_tabla = tk.Frame(win)
    frame_tabla.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    columnas = ("codigo", "nombre", "existencia", "proveedor", "precio")
    tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings")
    for col in columnas:
        tabla.heading(col, text=col.capitalize())
        tabla.column(col, width=120)
    tabla.pack(fill=tk.BOTH, expand=True)

    def cargar_productos():
        for fila in tabla.get_children():
            tabla.delete(fila)
        productos = listar_productos()
        for prod in productos:
            tabla.insert("", tk.END, values=(
                prod["codigo"], prod["nombre"], prod["existencia"], prod["proveedor"], prod["precio"]
            ))

    cargar_productos()

    # Función para agregar producto
    def agregar_producto():
        codigo = simpledialog.askstring("Nuevo Producto", "Código:")
        if not codigo:
            return
        nombre = simpledialog.askstring("Nuevo Producto", "Nombre:")
        if not nombre:
            return
        try:
            existencia = int(simpledialog.askstring("Nuevo Producto", "Existencia:"))
            proveedor = simpledialog.askstring("Nuevo Producto", "Proveedor:")
            precio = float(simpledialog.askstring("Nuevo Producto", "Precio:"))
        except (TypeError, ValueError):
            messagebox.showerror("Error", "Datos inválidos para existencia o precio")
            return

        crear_producto(codigo, nombre, existencia, proveedor, precio)
        messagebox.showinfo("Éxito", "Producto creado correctamente")
        cargar_productos()

    # Función para eliminar producto
    def eliminar_producto_ui():
        seleccionado = tabla.selection()
        if not seleccionado:
            messagebox.showwarning("Atención", "Seleccione un producto para eliminar")
            return
        item = tabla.item(seleccionado)
        codigo = item['values'][0]

        if messagebox.askyesno("Confirmar", f"¿Seguro que desea eliminar el producto {codigo}?"):
            eliminado = eliminar_producto(codigo)
            if eliminado:
                messagebox.showinfo("Éxito", "Producto eliminado")
                cargar_productos()
            else:
                messagebox.showerror("Error", "No se pudo eliminar el producto")

    # Función para editar producto
    def editar_producto_ui():
        seleccionado = tabla.selection()
        if not seleccionado:
            messagebox.showwarning("Atención", "Seleccione un producto para editar")
            return
        item = tabla.item(seleccionado)
        codigo = item['values'][0]

        # Pedir nuevos datos (dejar en blanco para no modificar)
        nuevo_nombre = simpledialog.askstring("Editar Producto", "Nuevo nombre:")
        nuevo_existencia = simpledialog.askstring("Editar Producto", "Nueva existencia:")
        nuevo_proveedor = simpledialog.askstring("Editar Producto", "Nuevo proveedor:")
        nuevo_precio = simpledialog.askstring("Editar Producto", "Nuevo precio:")

        # Convertir datos
        nueva_existencia_val = None
        nuevo_precio_val = None
        if nuevo_existencia:
            try:
                nueva_existencia_val = int(nuevo_existencia)
            except ValueError:
                messagebox.showerror("Error", "Existencia debe ser un número entero")
                return
        if nuevo_precio:
            try:
                nuevo_precio_val = float(nuevo_precio)
            except ValueError:
                messagebox.showerror("Error", "Precio debe ser un número decimal")
                return

        actualizado = actualizar_producto(
            codigo,
            nuevo_nombre=nuevo_nombre if nuevo_nombre else None,
            nueva_existencia=nueva_existencia_val,
            nuevo_proveedor=nuevo_proveedor if nuevo_proveedor else None,
            nuevo_precio=nuevo_precio_val
        )

        if actualizado:
            messagebox.showinfo("Éxito", "Producto actualizado")
            cargar_productos()
        else:
            messagebox.showerror("Error", "No se pudo actualizar el producto")

    # Función para editar existencia (sumar/restar)
    def editar_existencia_ui():
        seleccionado = tabla.selection()
        if not seleccionado:
            messagebox.showwarning("Atención", "Seleccione un producto para modificar existencia")
            return
        item = tabla.item(seleccionado)
        codigo = item['values'][0]

        try:
            cantidad = int(simpledialog.askstring("Editar Existencia", "Cantidad a agregar (+) o restar (-):"))
        except (TypeError, ValueError):
            messagebox.showerror("Error", "Ingrese un número válido")
            return

        resultado = editar_existencia_producto(codigo, cantidad)
        if resultado:
            messagebox.showinfo("Éxito", "Existencia modificada")
            cargar_productos()
        else:
            messagebox.showerror("Error", "No se pudo modificar la existencia (no puede ser negativa)")

    # Botones
    frame_botones = tk.Frame(win)
    frame_botones.pack(pady=10)

    btn_agregar = tk.Button(frame_botones, text="Agregar Producto", command=agregar_producto)
    btn_agregar.grid(row=0, column=0, padx=5)

    btn_editar = tk.Button(frame_botones, text="Editar Producto", command=editar_producto_ui)
    btn_editar.grid(row=0, column=1, padx=5)

    btn_eliminar = tk.Button(frame_botones, text="Eliminar Producto", command=eliminar_producto_ui)
    btn_eliminar.grid(row=0, column=2, padx=5)

    btn_existencia = tk.Button(frame_botones, text="Modificar Existencia", command=editar_existencia_ui)
    btn_existencia.grid(row=0, column=3, padx=5)

    win.mainloop()
