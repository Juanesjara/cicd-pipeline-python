# app/calculadora.py
"""
Módulo de operaciones matemáticas básicas.

Este módulo proporciona funciones para realizar operaciones
aritméticas simples como suma, resta, multiplicación y división.
Incluye validación para evitar divisiones por cero.

Módulo de operaciones matemáticas básicas.

Funciones disponibles:
- sumar(a, b): retorna la suma de dos números
- restar(a, b): retorna la resta de dos números
- multiplicar(a, b): retorna el producto de dos números
- dividir(a, b): retorna la división de dos números

Lanza:
- ZeroDivisionError: si se intenta dividir por cero.

Autor: Tu Nombre
"""

AUTOR = "defrancov, jlmurillob, jejaramilr"


def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b
