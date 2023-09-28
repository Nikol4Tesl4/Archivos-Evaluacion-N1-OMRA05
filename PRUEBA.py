print("-Codigo 1:")
# Imprime el encabezado
print("Evaluación N°1 Redes Avanzadas 1")
print("Integrantes: Carlos Garay")

######################################################
print("-Codigo 2:")

# Solicita información al usuario
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
codigo_seccion = input("Ingresa tu código de sección: ")
sede = input("Ingresa tu sede: ")

# Muestra la información en pantalla
print("\Información ingresada:")
print("Nombre:", nombre)
print("Apellido:", apellido)
print("Código de Sección:", codigo_seccion)
print("Sede:", sede)

###########################################################

print("-Codigo 3:")

while True:
    # Solicita al usuario ingresar un número de ACL IPv4
    numero_acl = input("Ingresa el número de ACL IPv4 (o 'q' para salir): ")

    # Verifica si el usuario quiere salir del programa
    if numero_acl.lower() == 'q':
        print("Saliendo del programa.")
        break

    # Verifica si es una ACL estándar
    if numero_acl.isdigit() and 1 <= int(numero_acl) <= 99:
        print("Es una ACL estándar.")

    # Verifica si es una ACL extendida
    elif numero_acl.isdigit() and 100 <= int(numero_acl) <= 199:
        print("Es una ACL extendida.")

    # Si no es ninguna de las anteriores, indica que no corresponde a una lista de acceso
    else:
        print("El número no corresponde a una lista de acceso.")
    