print("Dime cuántas monedas de 1 euros tienes")
mon1 = int(input())
print("Dime cuántas monedas de 2 euros tienes")
mon2 = int(input())
print("Dime cuántas monedas de 50 céntimos tienes")
cent50 = int(input())
print("Dime cuántas monedas de 20 céntimos tienes")
cent20 = int(input())
print("Dime cuántas monedas de 10 céntimos tienes")
cent10 = int(input())

centimos_totales = (cent50*50)+(cent20*20)+(cent10*10)
euros_totales = mon1 + (mon2*2)
centimos_a_euros = int(centimos_totales/100)
centimos_restantes = centimos_totales%100

print("Tienes un total de", euros_totales+centimos_a_euros, "euros y", centimos_restantes,"céntimos")