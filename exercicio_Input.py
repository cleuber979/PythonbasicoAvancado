nome = input("Digite seu nome:")
print("Praze em conhecer por favor continue inserindo os dados :" , nome)

sobrenome = input("Por favor digite seu sobrenome completo:" )
print("Obrigado por continuar seu cadastro conosco ",  sobrenome )

idade = input("Por favor digite sua idade: ")
print("Obrigado por continuar seu cadastro conosco ", idade)
int_idade = int(idade)
ano_nascimento = input("por favor digite o ano que você nasceu :")
print("Obrigado por continuar seu cadastro conosco ", ano_nascimento)

if(int_idade > 18):
    int_idade = int(idade)
    print("O usuário é maior de idade")
else:
    print("Não e possível continuar o cadastro o usuário e menor de idade ")

altura = input("digite sua altura por favor ")
print("Obrigado por finalizar o cadastro conosco!")

