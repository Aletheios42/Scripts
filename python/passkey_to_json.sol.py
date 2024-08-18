# Solicitar la clave privada en formato hexadecimal desde la entrada estándar
hex_key = input("Introduce tu clave privada en formato hexadecimal: ")

# Convertir la clave privada hexadecimal a una lista de enteros
byte_array = [int(hex_key[i:i+2], 16) for i in range(0, len(hex_key), 2)]

# Imprimir la lista de enteros
print(byte_array)

