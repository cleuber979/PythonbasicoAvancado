# Operadores in e bot in 
# Strings são interaveis 
# 0 1 2 3 4 5 6 
# c l e u b e r
#-7-6-5-4-3-2-1

nome = 'cleuber'
print(nome[2])
print(nome[-5])

print('uber' in nome)
print('zero' in nome)
print(10* '-')
print('uber' not in nome)
print('zero' not in nome)


nome = input('Digite seu nome:  ')
encontrar = input('Digite o que deseja encontrar:  ')

if encontrar in nome:
    print(f'{encontrar}está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')	


