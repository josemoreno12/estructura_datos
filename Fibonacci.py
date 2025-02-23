def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        secuencia = fibonacci(n - 1)  
        return secuencia + [secuencia[-1] + secuencia[-2]] 

if __name__ == "__main__":
    n = 31
    print(fibonacci(n))
