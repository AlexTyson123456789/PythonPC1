#Problema 7:
#Realiza un programa que lea dos números por teclado y permite elegir entre 3 opciones en un menú:
#- Mostrar una suma de los dos números
#- Mostrar una resta de los dos números (el primero menos el segundo)
#- Mostrar una multiplicación de los dos números
#- En caso de introducir una opción inválida, el programa informará de que no es correcta.

#SOLUCION:

# Solicitar al usuario dos números
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

# Menú de opciones
print("\nMenú:")
print("1. Mostrar la suma de los dos números")
print("2. Mostrar la resta de los dos números (el primero menos el segundo)")
print("3. Mostrar la multiplicación de los dos números")

# Solicitar al usuario que elija una opción
opcion = input("Ingrese el número de la opción deseada (1, 2, o 3): ")

# Realizar la operación según la opción seleccionada
if opcion == "1":
    resultado = numero1 + numero2
    print(f"La suma de los dos números es: {resultado}")
elif opcion == "2":
    resultado = numero1 - numero2
    print(f"La resta de los dos números es: {resultado}")
elif opcion == "3":
    resultado = numero1 * numero2
    print(f"La multiplicación de los dos números es: {resultado}")
else:
    print("Opción no válida. Por favor, ingrese 1, 2 o 3.")  # SE PUEDE ELEGIR CUALQUIER A DE LAS OPCIONES


