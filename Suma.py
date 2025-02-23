def sumar_lista(arr):
    if not arr:
        return 0
    return arr[0] + sumar_lista(arr[1:]) 

numeros = [86, 33, 61, 25, 28, 14]
resultado = sumar_lista(numeros)
print(f"Suma de la lista: {resultado}")
