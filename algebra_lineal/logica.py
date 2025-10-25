import numpy as np 
from utilidades import mostrar_matriz_texto

# Inversa 
def calcular_inversa(A):
    det = np.linalg.det(A)
    texto = f"\nEl Determinante es: {round(det, 4)} \n\n"

    #abs devuelve el valor absoluto 
    if abs(det) < 1e-10:
        texto += "Esta matriz no tiene inversa (El determinantes es 0)."
        return None, texto
    else: 
        A_inv = np.linalg.inv(A)
        texto += mostrar_matriz_texto(A_inv, "Matriz Inversa")
        return A_inv, texto
    
'''Operacion de multiplicacion'''

def multiplicar_matrices(A, B):
    #Debe tener el mismo numero de columnas de a por filas de b
    if A.shape[1] != B.shape[0]:
            texto = (f"No se pueden multiplicar matrices {A.shape[0]}x{A.shape[1]} y {B.shape[0]}x{B.shape[1]}\n"
                     f"Las columnas de A ({A.shape[1]}) deben ser iguales a las filas de B ({B.shape[0]})")
            return None, texto
        
    # Multiplicar con dot=producto
    C = np.dot(A, B)
    texto = mostrar_matriz_texto(C, f"Resultado (A x B) Matriz {C.shape[0]}x{C.shape[1]}")
    texto += "\n La multipliacion de matrices ha sido exitosamente"
    return C, texto

'''Sistemas de Ecuaciones'''

def gauss_jordan(A, b):
    """Resuelve por Gauss-Jordan y retorna texto del proceso"""
    n = len(b)
    Ab = np.column_stack([A.copy(), b.copy()])
    texto = ""
    
    for i in range(n):
        max_fila = i
        for k in range(i + 1, n):
            if abs(Ab[k][i]) > abs(Ab[max_fila][i]):
                max_fila = k
        
        if max_fila != i:
            Ab[[i, max_fila]] = Ab[[max_fila, i]]
            
        if abs(Ab[i][i]) < 1e-10:
            continue
        
        Ab[i] = Ab[i] / Ab[i][i]
        for k in range(n):
            if k != i and abs(Ab[k][i]) > 1e-10:
                Ab[k] = Ab[k] - Ab[k][i] * Ab[i]
    
    return analizar_solucion_texto(Ab, n, texto)

def regla_cramer(A, b):
    """Resuelve por Cramer y retorna texto"""
    texto = "\n--- REGLA DE CRAMER ---\n\n"
    det_A = np.linalg.det(A)
    texto += f"Determinante de A: {round(det_A, 4)}\n\n"
    
    if abs(det_A) < 1e-10:
        return None, "indeterminado", texto + "Determinante = 0, no se puede usar Regla de Cramer"
    
    n = len(b)
    soluciones = []
    
    for i in range(n):
        A_i = A.copy()
        A_i[:, i] = b
        det_i = np.linalg.det(A_i)
        sol = det_i / det_A
        texto += f"x{i+1}: Det(A{i+1}) = {round(det_i, 4)}\n"
        soluciones.append(sol)
    
    return soluciones, "única", texto

def analizar_solucion_texto(Ab, n, texto_previo):
    """Analiza solución y retorna resultado"""
   #Toma todas las filas y todas las columnas excepto la última
    A_red = Ab[:, :-1]
    b_red = Ab[:, -1]
    
    rango_A = np.linalg.matrix_rank(A_red)
    rango_Ab = np.linalg.matrix_rank(Ab)
    
    if rango_A < rango_Ab:
        return None, "sin solución", texto_previo
    elif rango_A == rango_Ab == n:
        return b_red[:n].tolist(), "única", texto_previo
    else:
        return None, "infinitas", texto_previo
