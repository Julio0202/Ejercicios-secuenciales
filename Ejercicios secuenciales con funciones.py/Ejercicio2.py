def imprimirArea(base:int,altura:int):
    return int(base*altura/2)
def imprimirPerimetro(base:int,altura:int):
    return int(base*2+altura*2)
base = int(input("Dime la base"))
altura = int(input("Dime la altura"))
print("El area del triangulo es",imprimirArea(base,altura))
print("El perimetro del triangulo es",imprimirPerimetro(base,altura))
def lista(base:int,altura:int):
    vdatos = []
    vdatos.append(imprimirArea(base,altura))
    vdatos.append(imprimirPerimetro(base,altura))
    return vdatos
print("La lista es", lista(base,altura))

