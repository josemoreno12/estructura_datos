def multiplicacion(a, b):
    if b == 0:
        return 0
    if b < 0:
        return -multiplicacion(a, -b) 
    return a + multiplicacion(a, b - 1)

if __name__ == "__main__":
    print(multiplicacion(36, 22))  
    print(multiplicacion(21, 8))  
    print(multiplicacion(-7, 5))  
    print(multiplicacion(7, -5))  
    print(multiplicacion(-7, -5))  
