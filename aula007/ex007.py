# --- EXERCICIO MÉDIA ARITMÉTICA

nome = input("Bom dia! Insira seu nome aqui:")
print ("Perfeito {}! Vamos calcular sua média?".format(nome))

# - Primeiro Semestre
s1 = float(input("Sua nota do 1º Semestre:"))
if s1 >= 7:
    print ("Parábens, {}, você está acima da média!".format(nome))
else:
    print ("Eita {}, precisamos melhorar sua nota!".format(nome))

# - Segundo Semestre
s2 = float(input("Sua nota do 2º Semestre:"))
if s2 >= 7:
    print ("Parábens, {}, você está acima da média!".format(nome))
else:
    print ("Eita {}, precisamos melhorar sua nota!".format(nome))

# - Média final
media = (s1 + s2) / 2
if media >= 7:
    print (("=" * 20))
    print ("Excelente {}, sua média final foi {}! Você passou!!!".format(nome, media))
    print (("=" * 20))
elif media < 6:
    print (("=" * 20))
    print ("Poxa {}, sua média final foi de apenas {}... Você reprovou!".format(nome, media))
    print (("=" * 20))