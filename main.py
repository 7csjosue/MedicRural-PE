"""Menu principal de MedicRural-PE."""
from inventario import (ARCHIVO, cargar_inventario, guardar_inventario,
                        registrar_medicamento, buscar_medicamento, listar_inventario)
from prioridades import mostrar_alertas
from reportes import generar_grafico, generar_reporte


def descargar_archivo():
    guardar_inventario()
    try:
        from google.colab import files
        files.download(ARCHIVO)
    except ImportError:
        print("El archivo esta guardado localmente como:", ARCHIVO)


def menu():
    cargar_inventario()
    while True:
        print("\n================================")
        print("       MEDICRURAL-PE")
        print("================================")
        print("1. Registrar medicamento")
        print("2. Buscar medicamento por codigo")
        print("3. Listar inventario ordenado")
        print("4. Mostrar alertas")
        print("5. Generar grafico de barras")
        print("6. Generar reporte TXT")
        print("7. Descargar archivo TXT")
        print("8. Salir")
        print("================================")
        opcion = input("Selecciona una opcion: ").strip()
        if opcion == "1":
            registrar_medicamento()
        elif opcion == "2":
            buscar_medicamento()
        elif opcion == "3":
            listar_inventario()
        elif opcion == "4":
            mostrar_alertas()
        elif opcion == "5":
            generar_grafico()
        elif opcion == "6":
            generar_reporte()
        elif opcion == "7":
            descargar_archivo()
        elif opcion == "8":
            guardar_inventario()
            print("Programa finalizado.")
            break
        else:
            print("Opcion incorrecta. Elige del 1 al 8.")


if __name__ == "__main__":
    menu()
