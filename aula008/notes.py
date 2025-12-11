import math
import random
import emoji

#--- Dá pra importar varias coisas de uma vez
from math import sqrt, floor, ceil

#---------------- Testezinho pa 
# Importa todo o modúlo
import vartest1

# Importa só uma variável
from vartest1 import n1

#---------------- A partir daqui é o que o guanabas ensina:

num = int (input ("Digite um número: "))

#--- Neste aqui eu uso a importação inteira de "math"
raiz = math.sqrt (num)

#--- Enquanto nesse eu uso só a importação de "sqrt" do modúlo "math"
raiz2 = sqrt (num)

#--- Nesse exemplo eu arrendondo a raiz quadrada pra cima usando "math.ceil(X)"
print ("A raiz quadrada de {} é {}. (Usando math.ceil(X))".format(num, math.ceil(raiz)))

print ("A raiz quadrada de {} é {:.2f}. (Usando :.2f)".format(num, raiz2))

#--- Isso aqui serve pra gerar um número inteiro entre 1 e 100, randint significa num inteiro randomico sla kkk
rdi = random.randint (1, 100)
print (rdi)

rdf = random.randrange (1, 100)
print (rdf, "🪴🪴")

print(emoji.emojize('Python is :thumbs_up:'))

