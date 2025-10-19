from openpyxl import load_workbook
from pathlib import Path

archivo_excel = Path(__file__).parent / 'archivos' / 'datos.xlsx'

def cargar_datos():
    libro = load_workbook(archivo_excel, data_only=True)
    clientes_hoja = libro['clientes']
    ventas_hoja = libro['ventas']

    # Cargar clientes en diccionario {codigo: {nombre, direccion}}
    clientes = {}
    for fila in clientes_hoja.iter_rows(min_row=2, max_col=3, values_only=True):
        codigo, nombre, direccion = fila
        clientes[codigo] = {
            "nombre": nombre,
            "direccion": direccion
        }

    # Cargar ventas en lista de diccionarios
    ventas = []
    for fila in ventas_hoja.iter_rows(min_row=2, max_col=4, values_only=True):
        codigo_producto, codigo_cliente, cantidad_productos, total_venta = fila
        ventas.append({
            "codigo_producto": codigo_producto,
            "codigo_cliente": codigo_cliente,
            "cantidad_productos": cantidad_productos,
            "total_venta": total_venta
        })

    return clientes, ventas

def ventas_por_cliente():
    clientes, ventas = cargar_datos()
    resumen = {}
    for v in ventas:
        codigo_cliente = v["codigo_cliente"]
        resumen[codigo_cliente] = resumen.get(codigo_cliente, 0) + (v["total_venta"] or 0)

    # Retorna lista de tuplas: (codigo_cliente, nombre_cliente, total_venta)
    return [(codigo, clientes.get(codigo, {}).get("nombre", "Desconocido"), total) for codigo, total in resumen.items()]

def ventas_por_producto():
    _, ventas = cargar_datos()
    resumen = {}
    for v in ventas:
        codigo_producto = v["codigo_producto"]
        resumen[codigo_producto] = resumen.get(codigo_producto, 0) + (v["cantidad_productos"] or 0)

    # Retorna lista de tuplas: (codigo_producto, cantidad_total)
    return list(resumen.items())
