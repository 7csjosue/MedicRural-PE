"""Registro, consulta y almacenamiento del inventario MedicRural-PE."""
import os
from datetime import datetime

ARCHIVO = "inventario_medicrural.txt"
medicamentos = []


def cargar_inventario():
    medicamentos.clear()
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                datos = linea.rstrip("\n").split("|")
                if len(datos) == 6:
                    try:
                        cantidad, minimo = int(datos[2]), int(datos[3])
                    except ValueError:
                        continue
                    medicamentos.append({
                        "codigo": datos[0], "nombre": datos[1],
                        "cantidad": cantidad, "minimo": minimo,
                        "establecimiento": datos[4], "fecha": datos[5]
                    })


def guardar_inventario():
    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        for m in medicamentos:
            archivo.write("|".join([
                m["codigo"], m["nombre"], str(m["cantidad"]),
                str(m["minimo"]), m["establecimiento"], m["fecha"]
            ]) + "\n")


def leer_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto and "|" not in texto and "\n" not in texto:
            return texto
        print("Ingresa un texto valido.")


def registrar_medicamento():
    print("\n--- REGISTRAR MEDICAMENTO ---")
    nombre = leer_texto("Nombre del medicamento o insumo: ")
    establecimiento = leer_texto("Establecimiento de salud: ")
    try:
        cantidad = int(input("Cantidad disponible: "))
        minimo = int(input("Cantidad minima necesaria: "))
        if cantidad < 0 or minimo < 0:
            print("Las cantidades no pueden ser negativas.")
            return
    except ValueError:
        print("Debes ingresar cantidades numericas.")
        return
    numero = max((int(m["codigo"][3:]) for m in medicamentos
                  if m["codigo"].startswith("MED") and m["codigo"][3:].isdigit()), default=0) + 1
    codigo = "MED" + str(numero).zfill(4)
    medicamento = {
        "codigo": codigo, "nombre": nombre, "cantidad": cantidad,
        "minimo": minimo, "establecimiento": establecimiento,
        "fecha": datetime.now().strftime("%d/%m/%Y %H:%M")
    }
    medicamentos.append(medicamento)
    guardar_inventario()
    print("\nMedicamento registrado correctamente. Codigo asignado:", codigo)
    if cantidad == 0:
        print("ALERTA CRITICA: No hay unidades disponibles.")
    elif cantidad <= minimo:
        print("ALERTA: Se necesita reponer este producto.")
    else:
        print("Stock suficiente segun el minimo registrado.")


def buscar_medicamento():
    codigo = input("\nIngresa el codigo del medicamento: ").strip()
    for m in medicamentos:
        if m["codigo"].lower() == codigo.lower():
            print("\n--- MEDICAMENTO ENCONTRADO ---")
            for clave, etiqueta in [("codigo", "Codigo"), ("nombre", "Nombre"),
                                   ("cantidad", "Cantidad"), ("minimo", "Cantidad minima"),
                                   ("establecimiento", "Establecimiento"), ("fecha", "Fecha de registro")]:
                print(etiqueta + ":", m[clave])
            print("Estado:", estado_medicamento(m))
            return
    print("No se encontro el medicamento.")


def estado_medicamento(m):
    if m["cantidad"] == 0:
        return "CRITICO"
    if m["cantidad"] <= m["minimo"]:
        return "REPOSICION NECESARIA"
    return "STOCK SUFICIENTE"


def listar_inventario():
    if not medicamentos:
        print("\nNo hay medicamentos registrados.")
        return
    print("\n--- INVENTARIO ORDENADO POR NOMBRE ---")
    for m in sorted(medicamentos, key=lambda item: item["nombre"].lower()):
        print("------------------------------")
        print("Codigo:", m["codigo"], "| Nombre:", m["nombre"])
        print("Cantidad:", m["cantidad"], "| Establecimiento:", m["establecimiento"])
        print("Estado:", estado_medicamento(m))
    print("------------------------------")
    print("Total de productos:", len(medicamentos))
