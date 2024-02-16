
#Introdução ao try/execept
#try -> tenta execultar o codigo 
#except -> ocorreu algum erro ao tentar executar


#print(1234)
#print(456) 
#float('a')

numero = input('Vou dobrar o numero que vc digitar : ')

try: 
    print('STR:',numero)
    numero_float = float(numero)
    print('FLOAT:',numero_float)
    print(f'O dobro de {numero} é {numero_float * 2}')
except:
    print('O valor digitado não é um numero')


#numero_float = float(numero)
#print(numero.isdigit())
#print(f'O dobro de {numero} é {numero_float * 2}')
