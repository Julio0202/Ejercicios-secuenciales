from cmath import sqrt
import math
def imprimirhip(cateto1:int,cateto2:int):
    return math.sqrt(cateto1*cateto1+cateto2*cateto2)
print("Dime el primer cateto")
cateto1 = int(input())
cateto2 = int(input())
print("La hipotenusa mide",imprimirhip(cateto1,cateto2))