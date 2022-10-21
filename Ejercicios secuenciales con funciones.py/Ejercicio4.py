def suma(num1:int,num2:int):
    return num1+num2
def resta(num1:int, num2:int):
    return num1-num2
def division(num1:int,num2:int):
    return num1/num2
def multiplicacion(num1:int,num2:int):
    return num1*num2
print("Dime dos numeros")
num1 = int(input())
num2 = int(input())

print("La suma es", suma(num1,num2))
print("La resta es", resta(num1,num2))
print("La división es", division(num1,num2))
print("La multiplicación es", multiplicacion(num1,num2))