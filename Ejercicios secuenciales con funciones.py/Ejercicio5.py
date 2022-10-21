def conversion(gradosfare:int):
    return (gradosfare-32)*5/9

print("Dime los grados F")
gradosfare = int(input())

print("La conversión es", conversion(gradosfare))