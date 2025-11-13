# --- EXERCICIO ANTECESSOR E SUCESSOR

n = int(input("Digite um número: "))
ant = n - 1
suc = n + 1

print (("=" * 20))
print ("Analisando o valor: {}, seu antecessor é {} e seu sucessor é {}.".format(n, ant, suc))
print (("=" * 20))

#--- Outra forma de fazer usando apenas uma variável:

print (("=" * 20))
print ("Analisando o valor: {}, seu antecessor é {} e seu sucessor é {}.".format(n, (n-1), (n+1)))
print (("=" * 20))

# Show de bola papai 👌