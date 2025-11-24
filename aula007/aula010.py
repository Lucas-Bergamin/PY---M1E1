dinero = float (input ("Quanto dinheiro você tem na carteira? R$"))
#- Dolar hoje tá 5,39 Reais kkk, osso

money = dinero / 5.39

print ("-" * 12)
print ("Com R${:.2f} você pode comprar US${:.2f}.".format(dinero, money))
print ("-" * 12)