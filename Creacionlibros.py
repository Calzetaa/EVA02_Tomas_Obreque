#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para registrar libros de prueba en la API demo.
Genera títulos, autores e ISBN aleatorios y los envía por POST.
"""

import requests
import random
import string
import time

# ===================== CONFIGURACIÓN =====================
URL_API = "http://library.demo.local/api/v1/books"
CLAVE_API = "cisco|es4l5D8y2zxSjpVRcZfgUYffwEqmWoKqZA3aH2MO74g"

HEADERS = {
    "X-API-KEY": CLAVE_API,
    "Accept": "application/json",
    "Content-Type": "application/json"
}

# ===================== FUNCIONES AUXILIARES =====================

def texto_aleatorio(longitud=7):
    """Devuelve una cadena aleatoria de letras."""
    return ''.join(random.choices(string.ascii_letters, k=longitud))

def isbn_aleatorio():
    """Genera un número ISBN falso de 9 dígitos."""
    return ''.join(random.choices(string.digits, k=9))

def generar_libro(base, intento):
    """Crea un diccionario con datos de un libro."""
    return {
        "id": base + intento,
        "title": f"Ejemplar {texto_aleatorio(5)}",
        "author": f"{texto_aleatorio(3)} {texto_aleatorio(6)}",
        "isbn": isbn_aleatorio()
    }

# ===================== PROCESO PRINCIPAL =====================

def main():
    base_id = 70000
    total = 50
    creados = 0

    print("=== Cargando libros a la biblioteca demo ===\n")

    for n in range(total):
        for intento in range(3):
            libro = generar_libro(base_id + n * 10, intento)
            try:
                res = requests.post(URL_API, headers=HEADERS, json=libro)
                if res.status_code == 200:
                    print(f"✅ Libro creado: {libro['title']} (ID {libro['id']})")
                    creados += 1
                    break
                else:
                    print(f"⚠️ Error {res.status_code} — nuevo intento...")
            except Exception as e:
                print(f"❌ Error de conexión: {e}")
            time.sleep(0.15)
        time.sleep(0.05)

    print(f"\nFinalizado. Libros cargados correctamente: {creados}/{total}")

# ===================== EJECUCIÓN =====================

if __name__ == "__main__":
    main()
