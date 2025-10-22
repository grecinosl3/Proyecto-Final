import tkinter as tk
from tkinter import ttk, messagebox
from clientes import listar_clientes, crear_cliente, actualizar_cliente, eliminar_cliente

def interfaz_clientes():
    win = tk.Toplevel()
    win.title("Gestión de Clientes")
    win.geometry("600x650")
    win.configure(bg="#f0f0f0")

    # ------- Tabla para listar clientes -------
    frame_tabla = tk.Frame(win)
    frame_tabla.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    columnas = ("codigo", "nombre", "direccion")
    tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings")
    for col in columnas:
        tabla.heading(col, text=col.capitalize())
        tabla.column(col, width=40)
    tabla.pack(fill=tk.BOTH, expand=True)

    def cargar_clientes():
        for fila in tabla.get_children():
            tabla.delete(fila)
        clientes = listar_clientes()
        for cliente in clientes:
            tabla.insert("", tk.END, values=(
                cliente["codigo"],
                cliente["nombre"],
                cliente["direccion"]
            ))

    cargar_clientes()

    # ------- Formulario agregar cliente -------
    frame_form = tk.LabelFrame(win, text="Agregar nuevo cliente", padx=7, pady=7)
    frame_form.pack(fill=tk.X, padx=10, pady=5)

    tk.Label(frame_form, text="Código:").grid(row=0, column=0, sticky="e")
    entry_codigo = tk.Entry(frame_form)
    entry_codigo.grid(row=0, column=1, pady=2)

    tk.Label(frame_form, text="Nombre:").grid(row=1, column=0, sticky="e")
    entry_nombre = tk.Entry(frame_form)
    entry_nombre.grid(row=1, column=1, pady=2)

    tk.Label(frame_form, text="Dirección:").grid(row=2, column=0, sticky="e")
    entry_direccion = tk.Entry(frame_form)
    entry_direccion.grid(row=2, column=1, pady=2)

    def agregar_cliente():
        codigo = entry_codigo.get().strip()
        nombre = entry_nombre.get().strip()
        direccion = entry_direccion.get().strip()

        if not codigo or not nombre or not direccion:
            messagebox.showwarning("Campos vacíos", "Todos los campos son obligatorios.")
            return
        
        crear_cliente(codigo, nombre, direccion)
        messagebox.showinfo("Cliente agregado", "Cliente agregado exitosamente.")
        cargar_clientes()
        entry_codigo.delete(0, tk.END)
        entry_nombre.delete(0, tk.END)
        entry_direccion.delete(0, tk.END)

    tk.Button(frame_form, text="Agregar Cliente", command=agregar_cliente,
              bg="#27ae60", fg="white").grid(row=3, column=0, columnspan=2, pady=5)

    # ------- Formulario editar cliente -------
    frame_editar = tk.LabelFrame(win, text="Editar cliente (por código)", padx=7, pady=7)
    frame_editar.pack(fill=tk.X, padx=10, pady=5)

    tk.Label(frame_editar, text="Código a editar:").grid(row=0, column=0, sticky="e")
    entry_cod_edit = tk.Entry(frame_editar)
    entry_cod_edit.grid(row=0, column=1, pady=2)

    tk.Label(frame_editar, text="Nuevo Nombre:").grid(row=1, column=0, sticky="e")
    entry_nuevo_nombre = tk.Entry(frame_editar)
    entry_nuevo_nombre.grid(row=1, column=1, pady=2)

    tk.Label(frame_editar, text="Nueva Dirección:").grid(row=2, column=0, sticky="e")
    entry_nueva_dir = tk.Entry(frame_editar)
    entry_nueva_dir.grid(row=2, column=1, pady=2)

    def editar_cliente():
        codigo = entry_cod_edit.get().strip()
        nuevo_nombre = entry_nuevo_nombre.get().strip()
        nueva_dir = entry_nueva_dir.get().strip()

        if not codigo:
            messagebox.showwarning("Campo obligatorio", "Debe ingresar el código del cliente.")
            return

        resultado, datos_anteriores = actualizar_cliente(codigo, nuevo_nombre if nuevo_nombre else None, nueva_dir if nueva_dir else None)

        if resultado:
            messagebox.showinfo("Cliente actualizado", f"Cliente actualizado.\n\nDatos anteriores:\nNombre: {datos_anteriores['nombre']}\nDirección: {datos_anteriores['direccion']}")
            cargar_clientes()
            entry_cod_edit.delete(0, tk.END)
            entry_nuevo_nombre.delete(0, tk.END)
            entry_nueva_dir.delete(0, tk.END)
        else:
            messagebox.showerror("No encontrado", "No se encontró cliente con ese código.")

    tk.Button(frame_editar, text="Actualizar Cliente", command=editar_cliente,
              bg="#2980b9", fg="white").grid(row=3, column=0, columnspan=2, pady=5)

    # ------- Eliminar cliente -------
    frame_eliminar = tk.LabelFrame(win, text="Eliminar cliente (por código)", padx=7, pady=7)
    frame_eliminar.pack(fill=tk.X, padx=10, pady=5)

    tk.Label(frame_eliminar, text="Código a eliminar:").grid(row=0, column=0, sticky="e")
    entry_cod_del = tk.Entry(frame_eliminar)
    entry_cod_del.grid(row=0, column=1, pady=2)

    def eliminar_cliente_interfaz():
        codigo = entry_cod_del.get().strip()

        if not codigo:
            messagebox.showwarning("Campo obligatorio", "Debe ingresar el código del cliente.")
            return

        if eliminar_cliente(codigo):
            messagebox.showinfo("Cliente eliminado", f"Cliente con código {codigo} eliminado.")
            cargar_clientes()
            entry_cod_del.delete(0, tk.END)
        else:
            messagebox.showerror("No encontrado", "No se encontró cliente con ese código.")

    tk.Button(frame_eliminar, text="Eliminar Cliente", command=eliminar_cliente_interfaz,
              bg="#c0392b", fg="white").grid(row=1, column=0, columnspan=2, pady=5)
