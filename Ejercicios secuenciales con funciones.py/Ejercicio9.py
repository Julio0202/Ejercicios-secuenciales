from re import I


def descuento(porcentaje:int,producto:int):
    return producto-producto*(porcentaje/100)
print("Dime lo que cuesta el producto")
producto = int(input())
print("Dime el porcentaje del descuento")
porcentaje = int(input())

print("En total costaría", descuento(porcentaje,producto))
