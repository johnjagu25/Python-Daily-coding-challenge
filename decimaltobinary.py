def DecimalToBinary(num): 
    i = 0
    decimal = ""
    while(num > 0):
        rem = num % 2
        decimal += str(rem)
        num = num // 2
        i += 1
    return decimal[::-1]
    
print(DecimalToBinary(24))
print(DecimalToBinary(7))