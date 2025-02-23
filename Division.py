def division(a, b):
    if b == 0:
        return "Error: No se puede dividir entre 0"  
      
    if (a < 0 and b > 0) or (a > 0 and b < 0):  
        return -division(abs(a), abs(b))  # Manejo de signos
    
    if abs(a) < abs(b):
        return 0  
      
    return 1 + division(abs(a) - abs(b), abs(b))  

if __name__ == "__main__":
    print(division(18, 24))  
    print(division(50, 5))  
    print(division(30, -6))  
    print(division(-30, 6))  
    print(division(-30, -6))  
    print(division(10, 0))  # Caso de división por cero
