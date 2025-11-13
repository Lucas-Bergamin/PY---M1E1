n1 = int(input('Digite um número:'))
n2 = int(input ('Digite outro número:'))
s = n1 + n2

#--- Modo antigo!
# print ('A soma entre ', n1, ' e ', n2, ' vale {}'.format(s))

#--- Modo novo e mais eficaz!
print ('A soma entre {} e {} vale {}.'.format(n1, n2, s))