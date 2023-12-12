import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def funcion(x):
    return x**4 - 3*x**3 + x**2 - 5*x + 2

def falsa_suposicion(funcionFalsa, xn, xp):
    resultados = []

    iteraciones = 0
    while True:
        fXn = funcionFalsa(xn)
        fXp = funcionFalsa(xp)
        
        # Evitar división por cero
        if fXp == fXn:
            break

        xe = (xp * fXn - xn * fXp) / (fXn - fXp)
        fXe = funcionFalsa(xe)

        prueba_convergencia = abs((xe - xp) / xe) if xe != 0 else 0

        resultados.append({
            "Iteración": iteraciones,
            "Xn": xn,
            "Xp": xp,
            "Xe": xe,
            "f(Xn)": fXn,
            "f(Xp)": fXp,
            "f(Xe)": fXe,
            "Prueba convergencia": prueba_convergencia
        })

        if  fXe == 0 or prueba_convergencia == 0 :
            break

        if fXe * fXn < 0:
            xp = xe
        else:
            xn = xe

        iteraciones += 1

    return pd.DataFrame(resultados)

# Prueba del método
#funcion, 0, 4, 3.126259
def graficarFuncion(funcion,xn,xp,objetivo):
    x_valores = np.linspace(xn,xp,1000)
    y_valores = funcion(x_valores)
    resultados = falsa_suposicion(funcion,xn,xp,objetivo)
    plt.plot(x_valores, y_valores, label='')
    plt.axhline(0, color='black',linewidth=3)
    plt.axvline(0, color='black',linewidth=3)
    plt.title('Método de la Falsa suposicion')
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.legend()
    plt.grid(True)
    plt.show()
    #Mostrar la tabla
    print(resultados)

xn_falsaSuposicion = 0
xp_falsaSuposicion = 3.21
objetivo_FalsaSuposicion = 3.126259

graficarFuncion(funcion,xn_falsaSuposicion,xp_falsaSuposicion,objetivo_FalsaSuposicion)

