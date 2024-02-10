#Fatiamento de strings
# 012345678
# ola mundo
#-987654321
#Fatiamento [i:f:p] [::]
#obs: : a função len retorna a qtd de caracteres da str

variavel = 'olá mundo'
print(len (variavel))
print(variavel[0:len(variavel):])
#segundo exemplo e o passo que e de um em um ou dois em dois
print(variavel[0:9:2])
# para escrever seu nome de tras para frente
print(variavel[::-1])
