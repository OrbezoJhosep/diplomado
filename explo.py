x = 24
g = 3
tolerancia = 0.1  # Define cuán cerca quieres que esté g*g de x

while abs(g * g - x) > tolerancia:  # Sigue iterando mientras la diferencia sea mayor que la tolerancia
    g_g = g * g
    x_div_g = x / g
    promedio = (g + x_div_g) / 2

    print("g.g = ", g_g)
    print("¿Está g.g lo suficientemente cerca a x?")
    print("En ese caso podríamos considerar el resultado =", g)
    print("Sino, vuelva a ejecutar esta celda")
    print("x/g = ", x_div_g)
    print("nuevo valor de g =", promedio)
    
    g = promedio  # Actualiza g para la siguiente iteración

print(f"El valor final aproximado de g es {g}")

