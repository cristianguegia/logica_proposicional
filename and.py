# Tabla de verdad para la compuerta AND
print("A B | A AND B")
print("------------")

# Posibles combinaciones de entrada
for A in [0, 1]:
    for B in [0, 1]:
        # Operación AND
        resultado = A and B
        # Imprimir fila de la tabla de verdad
        print(f"{A} {B} |   {resultado}")

