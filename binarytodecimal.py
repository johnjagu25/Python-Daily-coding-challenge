# Same as Binary to Decimal conversion
def binaryToDecimal(binary): 
    decimal = i = 0;  
    while binary > 0:
        dec = binary % 10
        decimal += dec * pow(2,i)
        binary //= 10
        i += 1  
        
    return decimal;  

print(binaryToDecimal(100)) 
print(binaryToDecimal(101)) 
print(binaryToDecimal(1001))