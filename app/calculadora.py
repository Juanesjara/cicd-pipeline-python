# app/calculadora.py
"""
Módulo de operaciones matemáticas básicas.

Este módulo proporciona funciones para realizar operaciones
aritméticas simples como suma, resta, multiplicación y división.
Incluye validación para evitar divisiones por cero.

Módulo de operaciones matemáticas básicas.
"""

AUTOR = "defrancov, jlmurillob, jejaramilr"

"""
- sumar(a, b): retorna la suma de dos números
"""


def sumar(a, b):
    return a + b


"""
- restar(a, b): retorna la resta de dos números
"""


def restar(a, b):
    return a - b


"""
- multiplicar(a, b): retorna el producto de dos números
"""


def multiplicar(a, b):
    return a * b


"""
- dividir(a, b): retorna la división de dos números
"""


def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b
