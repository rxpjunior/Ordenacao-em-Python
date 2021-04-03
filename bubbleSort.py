def ordena(lista):
    tamanho = len(lista)
    
    for x in range(1, tamanho):
        for y in range(tamanho - 1):
           if lista[y] > lista[y+1]:
               aux = lista[y]
               lista[y] = lista[y + 1]
               lista[y + 1] = aux
    return lista


lista = [3,4,0,1]
print(ordena(lista))


