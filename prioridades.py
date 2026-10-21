"""Filtrado y priorizacion funcional de medicamentos en riesgo."""
from inventario import medicamentos


def medicamentos_criticos():
    return list(filter(lambda m: m["cantidad"] == 0, medicamentos))


def medicamentos_reposicion():
    return list(filter(lambda m: 0 < m["cantidad"] <= m["minimo"], medicamentos))


def resumen_prioridades():
    """Transforma los productos con alertas en textos ordenados por urgencia."""
    criticos = list(map(lambda m: "CRITICO: " + m["nombre"] + " - " + m["establecimiento"] + " - Sin existencias", medicamentos_criticos()))
    reposicion = list(map(lambda m: "REPOSICION: " + m["nombre"] + " - " + m["establecimiento"] + " - Cantidad: " + str(m["cantidad"]), medicamentos_reposicion()))
    return criticos + reposicion


def mostrar_alertas():
    if not medicamentos:
        print("\nNo hay medicamentos registrados.")
        return
    print("\n--- ALERTAS DE DESABASTECIMIENTO ---")
    alertas = resumen_prioridades()
    if not alertas:
        print("No hay alertas segun los minimos registrados.")
    for alerta in alertas:
        print(alerta)
