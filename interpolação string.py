# Interpolação básica de String
# s - string
# d e i - int
#f- float
#x e X - hexadecimal (0123456789ABCDEF)
#"""

nome = 'cleuber'
preco = 1000.956812547
variavel = '%s, o preço e de R$%.2f' % (nome,preco)
print(variavel)
print('O hexadecimal de %d e %04X' % (1500,1500))