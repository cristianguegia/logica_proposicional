# Tabla de verdad para la expresión (p AND q) OR (NOT p AND NOT q)
print("p q | (p AND q) OR (NOT p AND NOT q)")
print("------------------------------------")

# Posibles combinaciones de entrada
for p in [0, 1]:
    for q in [0, 1]:
        # Operación NOT
        not_p = int(not p)
        not_q = int(not q)
        
        # Operaciones AND
        p_and_q = p and q
        not_p_and_not_q = not_p and not_q
        
        # Operación OR
        resultado = p_and_q or not_p_and_not_q
        
        # Imprimir fila de la tabla de verdad
        print(f"{p} {q} |         {resultado}")
