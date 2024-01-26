#Operadores lógicos 
# and (e) or (ou) not (não)
# and - todas as condições precisam ser verdadeiras
#também existe o tipo noneque e usado para representar um não valor 

entrada = input('Você deseja [E]ntrar [S]air ')
senha_digitada = input('Senha: ')

senha_permitida='12345'
#If = True

if entrada == 'E' and senha_digitada== senha_permitida:
    print('Entrar')
else:
    print('Sair')  