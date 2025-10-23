import math

# --- Combinaciones ---

# - Combinacion con repeticion
def calcular_combinacion_sin_repeticion(n, r):
    if r > n or n < 0 or r < 0:
        return "Valores inválidos"
    return math.comb(n, r)

# - Combinacion con repeticion
def calcular_combinacion_con_repeticion(n, r):
    if n <= 0 or r < 0:
        return "Valores inválidos"
    return math.comb(n + r - 1, r)

# --- Permutaciones ---

#Permutacion sin repeticion
def calcular_permutacion_sin_repeticion(n, r):
    if r > n or n < 0 or r < 0:
        return "Valores inválidos"
    return math.perm(n, r)

#Permutacion con repeticion
def calcular_permutacion_con_repeticion(n, r):
    if n <= 0 or r < 0:
        return "Valores inválidos"
    return n ** r

# --- Conjuntos ---
def operar_conjuntos(conjunto1, conjunto2, operacion='union'):
    if operacion == 'union':
        return conjunto1.union(conjunto2)
    elif operacion == 'interseccion':
        return conjunto1.intersection(conjunto2)
    elif operacion == 'diferencia':
        return conjunto1.difference(conjunto2)
    else:
        return "Operación no válida"
    
# --- MCD ---
def calcular_mcd(num1, num2):
    return math.gcd(num1, num2)