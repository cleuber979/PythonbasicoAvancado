# Operadores lógicos 
# and (e) or (ou) not (não)
# or - Qualquer condição verdadeira avalia toda a expressão como verdadeira.
# Se qualquer valor for considerado verdaddeiro, a expressão inteira será avaliada naquele valor.
# São consideradas falsy (as expressões que vc já viu)
# 0 0.0 ' ' False
# Também existe o tipo None que é usado para representar um não valor

entrada = input('Você deseja [E]ntrar [S]air ')
senha_digitada = input('Senha: ')

senha_permitida='12345'
#If = True

if (entrada == 'E' or entrada == 'e') and senha_digitada== senha_permitida:
    print('Entrar')
else:
    print('Sair')  
