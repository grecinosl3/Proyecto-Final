import openpyxl
from pathlib import Path

archivo_excel = Path(__file__).parent / 'archivos' / 'datos.xlsx'

#Listar Ventas
def listar_ventas():
    libro = openpyxl.load_workbook(archivo_excel)
    hoja = libro["ventas"]
    ventas = []

    for numero_fila in range(2, hoja.max_row + 1 ):
        venta = {
            "codigo producto": hoja.cell(row=numero_fila, column=1).value,
            "codigo cliente": hoja.cell(row=numero_fila, column=2).value,
            "cantidad producto": hoja.cell(row=numero_fila, column=3).value,
            "total ventas": hoja.cell(row=numero_fila, column=4).value,
        }
        ventas.append(venta)
    libro.close()
    return ventas

#Crear Venta
def crear_venta(codigo_producto, codigo_cliente, cantidad_producto, total_ventas): 
    libro = openpyxl.load_workbook(archivo_excel)
    hoja = libro["ventas"]

    proxima_fila = hoja.max_row + 1

    hoja.cell(row=proxima_fila, column=1).value = codigo_producto
    hoja.cell(row=proxima_fila, column=2).value = codigo_cliente
    hoja.cell(row=proxima_fila, column=3).value = cantidad_producto
    hoja.cell(row=proxima_fila, column=4).value = total_ventas

    libro.save(archivo_excel)
    libro.close()

#Anular venta
def anular_venta(codigo_producto):
    libro = openpyxl.load_workbook(archivo_excel)
    hoja = libro["ventas"]

    for i, fila in enumerate(hoja.iter_rows(min_row=2), start=2):
        if str(fila[0].value).strip() == str(codigo_producto).strip:
            hoja.delete_rows(i)
            libro.save(archivo_excel)
            libro.close()
            return True #Venta Eliminada
    libro.close()
    return False #No fue encontrado