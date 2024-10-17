# Tabla de verdad para la compuerta NOT
print("A | NOT A")
print("---------")

# Posibles valores de entrada
for A in [0, 1]:
    # Operación NOT
    resultado = not A
    # Convertir el resultado booleano a entero (0 o 1)
    resultado = int(resultado)
    # Imprimir fila de la tabla de verdad
    print(f"{A} |   {resultado}")
