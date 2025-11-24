#--- EXERCICIO DOBRO, TRIPLO E RAIZ QUADRADA

n = int(input("Digite um número:"))
dobro = n * 2
triplo = n * 3
raiz = n ** 0.5

""" #--- Feito sem usar .format
print (f"O dobro de {n} vale {dobro}. \nO triplo de {n} vale {triplo}. \nA raiz quadrada de {n} é {raiz}.")
"""

#--- Feito usando .format
print ("O dobro de {} vale {}. \nO triplo de {} vale {}. \nA raiz quadrada de {} é {:.2f}.".format(n, dobro, n, triplo, n, raiz))


