# --- EXERCICIO ALUGUEL DE CARROS

# dia = R$60,00 / km = R$0,15

dia = int (input ("Quantos dias alugados? "))
km = int (input ("Quantos Km rodados? "))
soma = (dia * 60) + (km * 0.15)

print ("-" * 30)
print ("O total a pagar é R${:.2f}.".format(soma))
print ("-" * 30)