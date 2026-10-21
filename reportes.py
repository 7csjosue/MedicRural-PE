"""Graficos y reportes TXT de MedicRural-PE."""
from datetime import datetime
from inventario import medicamentos
from prioridades import resumen_prioridades


def generar_grafico():
    if not medicamentos:
        print("\nNo hay datos para generar el grafico.")
        return
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("Instala matplotlib para generar el grafico.")
        return
    nombres = [m["nombre"] for m in medicamentos]
    cantidades = [m["cantidad"] for m in medicamentos]
    plt.figure(figsize=(10, 5))
    barras = plt.bar(nombres, cantidades)
    plt.title("Inventario de MedicRural-PE")
    plt.xlabel("Medicamentos e insumos")
    plt.ylabel("Unidades disponibles")
    plt.xticks(rotation=25, ha="right")
    plt.grid(axis="y", linestyle="--", alpha=0.3)
    for barra in barras:
        altura = barra.get_height()
        plt.text(barra.get_x() + barra.get_width() / 2, altura,
                 str(int(altura)), ha="center", va="bottom")
    plt.tight_layout()
    plt.show()
    print("Grafico generado correctamente.")


def generar_reporte():
    if not medicamentos:
        print("\nNo hay medicamentos para generar el reporte.")
        return
    with open("reporte_medicrural.txt", "w", encoding="utf-8") as archivo:
        archivo.write("REPORTE MEDICRURAL-PE\n")
        archivo.write("Fecha: " + datetime.now().strftime("%d/%m/%Y %H:%M") + "\n\n")
        archivo.write("INVENTARIO COMPLETO\n")
        for m in medicamentos:
            archivo.write(f'{m["codigo"]} - {m["nombre"]} - {m["cantidad"]} unidades\n')
        archivo.write("\nALERTAS POR PRIORIDAD\n")
        for alerta in resumen_prioridades():
            archivo.write(alerta + "\n")
        archivo.write("\nTotal de unidades: " + str(sum(m["cantidad"] for m in medicamentos)) + "\n")
    print("Reporte generado: reporte_medicrural.txt")
