euros = 0
cent = 0
euros_total = 0
centimos_totales = 0
print("Dime monedas de 1 euros tienes")
euro1 = int(input())
print("Dime cuantas monedas de 2 euros tienes")
euro2 = int(input())
print("Dime cuantas monedas de 50 centimos tienes")
cent50 = int(input())
print("DIme cuantas monedas de 20 centimos tienes")
cent20 = int(input())
print("Dime cuantas monedas de 10 centimos tienes")
cent10 = int(input())
if cent50>=2:
    euros = cent50/2
    cent += (cent50*50)%2
if cent20>=5:
    euros += cent20/5
    cent += (cent20*20)%5
if cent10>=10:
    euros += cent10/10
    cent += (cent10*10)%10

euros_total = euros + euro1 + (euro2*2)
print("Tienes un total de", int(euros_total), "y", cent, "centimos")