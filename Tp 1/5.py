def romano_a_decimal(romano):
    valores = {
        'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100,
        'D': 500, 'M': 1000
    }

    if not romano:
        return 0

    if len(romano) == 1:
        return valores[romano[0]]

    primero = valores[romano[0]]
    segundo = valores[romano[1]]

    if primero < segundo:
        return (segundo - primero) + romano_a_decimal(romano[2:])
    else:
        return primero + romano_a_decimal(romano[1:])

while True:
    numero = input("Ingrese un número romano (o 'salir'): ")

    if numero.lower() == "salir":
        break

    print("Decimal:", romano_a_decimal(numero))