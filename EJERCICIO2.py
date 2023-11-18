#Problema 2:
#En los Estados Unidos, se acostumbra dejar una propina a su mesero después de cenar en un restaurante, generalmente una cantidad igual al 15% o más del costo de su comida.
#Escriba un programa que pregunte al usuario cuánto fue su consumo en el restaurante y que porcentaje de propina desea dejar al mesero. Su programa debe devolver la cantidad 
#de dinero a dejar como propina.

#SOLUCION:

# Primeor se solicitar al usuario el costo y el porcentaje de propina de cada comida:
costo_comida = float(input("Ingrese el costo de la comida: $"))
porcentaje_propina = float(input("Ingrese el porcentaje de propina que desea dejar (%): "))

# Calcular la cantidad de dinero a dejar como propina
propina = (porcentaje_propina / 100) * costo_comida    #se deja el 15%.

# Mostrar la cantidad de dinero a dejar como propina
print(f"El dinero en propina a dejar es: ${propina:.2f}")

