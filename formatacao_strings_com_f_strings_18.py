#Formatação basica de stringstream
# s - string
# d- int
# f - float
# .<número de digitos>f
# x ou X - hexadecimal 
#(caractere ) (><')(quantidade)
# > - esquerda 
# < - Direita 
# ^ - centro
# Sinal - + ou - 
# EX.: 0>-100,1f
#conversion flags - !r !s !f 

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel:0^10}')
print(f'{1000.4265212395875:0=10,.1f}')
print(f'O Hexadecimal de 1500 e {1500:08X}')
print(f'{variavel!r}')
