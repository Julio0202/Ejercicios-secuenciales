def porcentaje10prod(prod1:int,prod2:int,prod3:int):
    return (prod1+prod2+prod3)*0.1
def sueldomasporcentaje(sueldo:int,prod1:int,prod2:int,prod3:int):
    return sueldo+((prod1+prod2+prod3)*0.1)

print("Dime los 3 productos respectivamente")
prod1 = int(input())
prod2 = int(input())
prod3 = int(input())
print("Dime el sueldo que tienes")
sueldo = int(input())
print("El 10% de los productos es", porcentaje10prod(prod1,prod2,prod3))
print("El sueldo más el el 10% es", sueldomasporcentaje(sueldo,prod1,prod2,prod3))