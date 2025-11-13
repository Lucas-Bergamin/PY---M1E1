""" --- Soma de dois números ---
n1 = int(input("Digite um número:"))
n2 = int(input("Digite outro número:"))
soma = n1 + n2

print ("A soma entre {} e {} é {}.".format(n1, n2, soma))
"""

""" --- Dissecando uma variável  ---
n = input("Digite algo: ")

print ("=" * 40)
print ("É númerico?", (n.isnumeric()))
print ("É alfabético?", (n.isalpha()))
print ("Está em UPPER?", (n.isupper()))
print ("=" * 40)
"""

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

soma = n1 + n2
sub = n1 - n2
mul = n1 * n2
pot = n1 ** n2
div = n1 / n2 
divint = n1 // n2
divrest = n1 % n2 

""" --- Versão com vários prints ---
print (("=" * 5), "Resultado", ("=" * 5))
print ("Você escolheu os números: {} e {}!".format(n1, n2))
print ("A soma entre esses números é: {}, a subtração: {}, e a multiplicação: {}.".format(soma, sub, mul)) 
print ("Que tal falar de divisão? \nA divisão de {} por {} é {:.2f}".format(n1, n2, div))
print ("Enquanto a divisão inteira é: {} e a potência: {}!".format(divint, pot))
print (("=" * 5), "Fim do cálculo", ("=" * 5))
"""

""" --- Tentativa falha de fazer usando apenas uma string...---
print (("=" * 5), "Resultado", ("=" * 5), "\nVocê escolheu os números: {} e {}!", "\nA soma entre esses números é: {}.", "\nA subtração: {}.", "\nE a divisão: {:.2f}.", ("=" * 5), "\nFim do cálculo", ("=" * 5).format(n1, n2, soma, sub, div), end= " ")
"""

# --- Chat GPT me mogou aqui :(
print(f"""===== Resultado =====
Você escolheu os números: {n1} e {n2}!
A soma entre esses números é: {soma}, a subtração: {sub}, e a multiplicação: {mul}.
Que tal falar de divisão? 
A divisão de {n1} por {n2} é {div:.2f}
Enquanto a divisão inteira é: {divint} e a potência: {pot}!
===== Fim do cálculo =====""")
