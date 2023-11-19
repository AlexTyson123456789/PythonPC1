#Problema 9:
#Escriba un programa que, dada una lista, devuelve una nueva lista cuyo contenido sea igual a la
#original pero invertida. Así, dada la lista ['Di', 'buen', 'día', 'a', 'papa'], deberá devolver ['papa', 'a', 'día', 'buen', 'Di'].

#SOLUCION:

# 1ro se define la lista original
lista_original = ['Di', 'buen', 'día', 'a', 'papa']

# luego se crear una nueva lista invertida
lista_invertida = list(reversed(lista_original))

# Mostrar la lista invertida
print("Lista original:", lista_original)
print("Lista invertida:", lista_invertida)

