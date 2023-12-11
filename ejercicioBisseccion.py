import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def funcion(x):
    return x**4 + 3*x**3 - x**2 - 5*x - 2

def metodoBiseccion(funcion, xn, xp, objetivo):
    if xn >= xp or funcion(xn) * funcion(xp) >= 0:
        print("Intervalo no válido. Asegúrate de que f(xn) y f(xp) tengan signos opuestos.")
        return pd.DataFrame(columns=["Iteración", "Xn", "Xp", "Xe", "f(Xe)", "Prueba de convergencia"])

    iteraciones = 0
    tabla = pd.DataFrame(columns=["Iteración", "Xn", "Xp", "Xe", "f(Xe)", "Prueba de convergencia"])
    
    while True:
        xe = xn + ((xp - xn) / 2)

        try:
            fx_valor = funcion(xe)
        except (ValueError, OverflowError):
            break

        pruebaConvergencia = abs((xe - xn) / xe) if xe != 0 else 0
        
        tabla = pd.concat([tabla, pd.DataFrame({
            "Iteración": [iteraciones],
            "Xn": [round(xn, 6)],
            "Xp": [round(xp, 6)],
            "Xe": [round(xe, 6)],
            "f(Xe)": [round(fx_valor, 6)],
            "Prueba de convergencia": [round(pruebaConvergencia, 6)]
        })], ignore_index=True)

        if abs(xe - objetivo) <= 1e-6 or funcion(xe) == 0 or pruebaConvergencia <= 1e-6:
            break

        if funcion(xe) * funcion(xn) < 0:
            xp = xe
        else:
            xn = xe

        iteraciones += 1

    return tabla

def graficarMetodoBiseccion(funcion, xn, xp, objetivo):
    x_valores = np.linspace(xn, xp, 1000)
    f_valores = funcion(x_valores)

    resultados_biseccion = metodoBiseccion(funcion, xn, xp, objetivo)

    plt.plot(x_valores, f_valores, label='f(x) = x^4 + 3*x^3 - x^2 - 5*x - 2')
    plt.title('Método de la Bisección con Aproximaciones y Prueba de Convergencia')
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Mostrar la tabla de resultados
    print(resultados_biseccion)

# Parámetros iniciales
xn_biseccion = 0
xp_biseccion = 2
objetivo_biseccion = 1.342923

# Llamar al método de bisección y graficar los resultados con la tabla
graficarMetodoBiseccion(funcion, xn_biseccion, xp_biseccion, objetivo_biseccion)
