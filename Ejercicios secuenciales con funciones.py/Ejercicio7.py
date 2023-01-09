def minutoshoras(minutos:int):
    return minutos/60
def minutossobrante(minutos:int):
    return minutos%60

print("Dime los minutos")
minutos=int(input())
print("La conversion es", int(minutoshoras(minutos)),"horas",minutossobrante(minutos),"minutos")