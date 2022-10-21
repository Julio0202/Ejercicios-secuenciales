def minutoshoras(minutos:int):
    return minutos/60
def minutossegundos(minutos:int):
    return minutos%60

print("Dime los minutos")
minutos=int(input())
print("La conversion es", int(minutoshoras(minutos)),"horas",minutossegundos(minutos),"minutos")