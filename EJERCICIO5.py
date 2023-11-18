#Problema 5:
#Escribir un programa que solicite al usuario que ingrese cuántos shows musicales ha visto en el
#último año y almacene ese número en una variable. A continuación, mostrar en pantalla un valor de
#verdad (True o False - tipo de datos booleanos) que indique si el usuario ha visto más de 3 shows.

#SOLUCION:

# se solicita al usuario la cantidad de shows musicales vistos en el último año
cantidad_shows = int(input("Ingrese cuántos shows musicales ha visto en el último año: "))

# se analiza si ha visto más de 3 shows
ha_visto_mas_de_tres_shows = cantidad_shows > 3

# por ultimo mostrar el resultado
print(f"¿Ha visto más de 3 shows musicales? {ha_visto_mas_de_tres_shows}")
