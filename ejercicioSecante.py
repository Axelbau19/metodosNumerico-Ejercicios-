import pandas as pd
def funcionSecante(x):
    return x**3-3*x**2+5*x+2

def metodoDelaSecante(funcionMetodo,xActual,xAnterior,objetivo):
    tablaSecante = []
    iteracionesSecante = 0
    while xActual != objetivo:
        fActual = funcionMetodo(xActual)
        fAnterior = funcionMetodo(xAnterior)
        evitarZero = fActual - fAnterior
        if evitarZero == 0:
            break
        xSiguiente = xActual - ((xActual - xAnterior) * fActual) / evitarZero
        fSiguiente = funcionSecante(xSiguiente)
       #Prueba de convergencia
        tablaSecante.append({
           "Iteracion": iteracionesSecante,
           "X actual" : xActual,
           "X anterior": xAnterior,
           "X siguiente":xSiguiente,
           "f(X actual)": fActual,
           "f(X anterior)": fAnterior,
           "f(X siguiente)": fSiguiente
       })
        if fSiguiente == 0:
            break
        xAnterior = xActual
        xActual = xSiguiente
        iteracionesSecante+=1

    return pd.DataFrame(tablaSecante)  

resultados_secante = metodoDelaSecante(funcionSecante,  0, -1, -0.328268)
print(resultados_secante)




        

