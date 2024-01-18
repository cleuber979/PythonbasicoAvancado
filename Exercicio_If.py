primeiro_Valor =input('Digite o primeiro valor a ser comparado: ')
valor1_digitado = int(primeiro_Valor)

segundo_valor= input('Digite o segundo valor a ser comparado: ')
valor2_digitado= int(segundo_valor)

if(valor1_digitado>valor2_digitado):
    print(f'{valor1_digitado} O valor que foi digitado primeiro e maior')
elif(valor1_digitado<valor2_digitado):
    print(f'{valor2_digitado} O segundo que foi digitado e valor maior')
else:
    print('Os valores são iguais !')    

