# Tabla de verdad para la compuerta OR
print("A B | A OR B")
print("------------")

# Posibles combinaciones de entrada
for A in [0, 1]:
    for B in [0, 1]:
        # Operación OR
        resultado = A or B
        # Imprimir fila de la tabla de verdad
        print(f"{A} {B} |   {resultado}")
