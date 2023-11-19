#Problema 10:
#Escriba un programa para imprimir una lista específica después de eliminar los elementos que se
#encuentran en la posición 0, 4 y 5. lista de muestra: ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
#Resultado esperado: ['Verde', 'Blanco', 'Negro']


#SOLUCION:

lista_muestra = ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']

# aqui se elimina en las posiciones 0, 4 y 5.
posiciones_a_eliminar = [0, 4, 5]
lista_resultante = [valor for i, valor in enumerate(lista_muestra) if i not in posiciones_a_eliminar]

# ahora se imprime el resultado
print("Lista original:", lista_muestra)
print("Nueva lista despues de eliminar elementos en las posiciones 0, 4 y 5:", lista_resultante)
