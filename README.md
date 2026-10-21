# MedicRural-PE

Prototipo en Python para controlar inventarios de medicamentos e insumos médicos y priorizar alertas de desabastecimiento en establecimientos rurales.

## Archivos
- `main.py`: menú y ejecución.
- `inventario.py`: registro, consulta, almacenamiento TXT y validaciones.
- `prioridades.py`: filtrado y transformación con `filter`, `map` y `lambda`.
- `reportes.py`: gráfico de barras y reporte TXT.
- `inventario_medicrural.txt`: datos persistentes (se crea o actualiza al guardar).

## Ejecutar
Desde la carpeta del proyecto: `python main.py`.
Para el gráfico se requiere `matplotlib` (`pip install matplotlib`).
En Google Colab, sube los cuatro archivos `.py` a la misma sesión y ejecuta `!python main.py` solo si tienes entrada interactiva compatible; alternativamente, usa el terminal de Colab o importa `main` y ejecuta `main.menu()` en una celda. La opción 7 descarga el TXT en Colab.

## GitHub
Sube los archivos fuente al mismo repositorio. Realiza commits conforme implementes y pruebes cambios reales. No subas `__pycache__`. Las capturas de ejecución y commits deben tomarse de tu proyecto real.
