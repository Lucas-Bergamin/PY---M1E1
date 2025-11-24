# --- EXERCICIO CALCULANDO DESCONTOS

preço = float (input ("Qual é o preço do produto? R$"))
desconto = preço / 20
final = preço - desconto

print ("-" * 20)
print ("O produto que custava R${}, na promoção com desconto de 5% vai custar R${:.2f}.".format(preço, final))
print ("-" * 20)

# --- jeito do guanabas

preço2 = float (input ("Qual é o preço do produto? R$"))
novo2 = preço2 - (preço * 5 / 100)

print ("-" * 20)
print ("O produto que custava R${}, na promoção com desconto de 5% vai custar R${:.2f}.".format(preço, novo2))
print ("-" * 20)