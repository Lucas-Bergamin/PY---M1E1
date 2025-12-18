# --- EXERCICIO CALCÚLO DE HIPOTENUSA SLA 

# - Meu jeito. (Conclusão: Muitas variáveis poluiram meu código, mas, funciona kkk)
n1 = float (input ("Comprimento do cateto oposto: "))
op = n1 ** 2
n2 = float (input ("Comprimento do cateto adjacente: "))
adj = n2 ** 2
hip = (op + adj) ** 0.5
print ("A hipotenusa vai medir: {:.2f}".format (hip))

print ("\n=== Versão 2 ===\n")

# Jeito mais clean. (Conclusão: Ficou melhor que o meu kkkk, economizou duas variáveis ent tá ótimo)
co = float (input ("Comprimento do cateto oposto: "))
ca = float (input ("Comprimento do cateto adjacente: "))
hipo = (co ** 2 + ca ** 2) ** 0.5

print ("A hipotenusa vai medir: {:.2f}".format (hipo))

print ("\n=== Versão 3 ===\n")

# Jeito usando módulo. (Conclusão: Simplifica ainda mais o código, provavelmente a melhor opção.)
from math import hypot

co1 = float (input ("Comprimento do cateto oposto: "))
ca2 = float (input ("Comprimento do cateto adjacente: "))
hi = hypot(co1, ca2)

print ("A hipotenusa vai medir: {:.2f}".format (hi))