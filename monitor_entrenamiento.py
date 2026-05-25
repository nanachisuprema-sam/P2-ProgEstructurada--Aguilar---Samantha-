"""
Nombre del Alumno: [Samantha Aguilar Cano]
Matrícula: [ux25ii277@]
Fecha: [25/may/26]
Examen Segundo Parcial - Programación Estructurada
"""
# ==========================================
# 1. IMPORTACIÓN DE BIBLIOTECAS ESTÁNDAR
# ==========================================

import datetime
import math
import random
import statistics
import sys
# ==========================================
# 2. DEFINICIÓN DE CONSTANTES
# ==========================================
MAX_EPOCHS = 10
UMBRAL_ERROR_CRITICO = 0.95
# ==========================================
# 3. FUNCIONES DEFINIDAS POR EL USUARIO
# ==========================================
def obtener_info_sistema():
 """
 Usa la biblioteca 'sys' para validar el entorno de ejecución.
 Requisitos: Realizar 3 llamadas distintas a la biblioteca 'sys'.
 """
 print("Información del sistema operativo:")
 plataforma= sys.platform #pal sistema opertivo (windowsssss)
 print("Plataforma:", plataforma)
 version=sys.version #muestra la version de python
 print("Version: ", version)
 ruta=sys.executable #ruta del ejecutable
 print("Ruta: ", ruta)
 pass
def simular_metricas_entrenamiento(cantidad_epochs):
 print("SIMULADOR ")
 fecha_inicio = datetime.datetime.now()
 print("Iniciando.... ", fecha_inicio.strftime("%d/%m/%Y %H:%M:%S"))
 eventos_posibles = [
   "Epoch exitoso",
   "Gradiente inestable",
   "Actualización de pesos",
    ]
 loss = random.uniform(0.1, 1.0)
 probabilidad_exito = random.random()
 evento = random.choice(eventos_posibles)
 lista_loss = [loss, probabilidad_exito, evento]
 latencia = 50.0 + (loss * 250.0)
 lista_latencias = [latencia]
 fecha_fin = datetime.datetime.now()
 duracion = fecha_fin - fecha_inicio
 print(f"Simulación terminada en: {duracion.total_seconds()} segundos.")
 return lista_loss, lista_latencias
def analizar_rendimiento(lista_loss):
    print("ANALIsis RENDIMIENTO")
    print(f"Loss obtenido: {lista_loss[0]:.4f}")
    print(f"Probabilidad de éxito: {lista_loss[1]:.4f}")
    print(f"Estado final: {lista_loss[2]}")
    return {"media_loss": statistics.mean([lista_loss[0], lista_loss[1]])}
def calcular_rmse(predicciones, reales):
 print("CÁLCULO DE RMSE")
 errores_cuadrados = [math.pow(p - r, 2) for p, r in zip(predicciones, reales)]
 suma_errores = math.fabs(sum(errores_cuadrados))
 media_errores = suma_errores / len(predicciones)
 rmse = math.sqrt(media_errores)
 print(f"RMSE calculado: {rmse:.4f}")

 pass
if __name__ == "__main__":
 print("=" * 50)
 print("INICIANDO")
 print("=" * 50)
 obtener_info_sistema()
 lista_loss, lista_latencias = simular_metricas_entrenamiento(MAX_EPOCHS)
 resultados = analizar_rendimiento(lista_loss, lista_latencias)
 reales = [loss + random.uniform(-0.05, 0.05) for loss in lista_loss]
 rmse = calcular_rmse(lista_loss, reales)
 print("\n--- DIAGNÓSTICO FINAL ---")
 media_final = resultados["media_loss"]
if media_final >= UMBRAL_ERROR_CRITICO:
    print(f"ERROR CRÍTICO: La media del loss ({media_final:.4f}) supera el umbral ({UMBRAL_ERROR_CRITICO}).")
    print("Terminando el programa por métricas críticas...")
    sys.exit(1)
else:
    print(f"Entrenamiento estable. Media del loss: {media_final:.4f}")
    print(f"RMSE final del modelo: {rmse:.4f}")
    print("\n=== SIMULACIÓN FINALIZADA CON ÉXITO ===")

"""
1. Uso de Objetos y Métodos: En tu código, al usar datetime.datetime.now(),
¿cuál es el objeto/clase y cuál es el método que estás llamando? 
Datetime es la clase, y now() es el metodo que se le está llamando

2. Diferenciación Técnica: ¿Qué diferencia existe en la sintaxis de tu código
al importar un módulo completo (ej: import math) versus importar un método
específico (ej: from math import sqrt) al momento de invocar sus funciones? Usando solo el import,
tienes que llamar al prefijo, mientras que agregando el from, puedes llamarlo directamente.


3. Flujo y Lógica: Describe brevemente la secuencia lógica de pasos que
implementaste para conectar los datos generados por tu función de
simulación con la función que calcula el error (RMSE).
=
simular_metricas_entrenamiento() genera lista_loss usando random.
    y random.uniform() y la retorna al programa principal.
En el programa principal se usa lista_loss directamente como 'predicciones'
y se genera añadiendo una pequeña variación aleatoria a cada valor.
   Ambas listas se pasan como argumentos a calcular_rmse(), que las recorre
    en paralelo para calcular la diferencia en cada punto y obtener
    el error cuadrático medio.


4. Mapeo de Tipos de Datos: Identifica al menos dos tipos de datos
complejos (colecciones) que utilizaste para organizar los resultados de tus
análisis y justifica por qué elegiste esa estructura en lugar de variables
simples.


5. Autoevaluación de Abstracción: Al utilizar las funciones de la biblioteca
statistics, ¿tuviste que programar la fórmula matemática matemática de la
desviación estándar? Relaciona esto con el concepto de Abstracción visto
en clase.=

Solo se llamó a statistics.stdev(lista_loss) y la biblioteca realizó el cálculo, 
con esto no hace falta realmente calcularlo manualmente, simplemente el programa recibe y entrega.
"""