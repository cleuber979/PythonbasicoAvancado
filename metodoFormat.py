a = 'A primeira letra do alfabeto'
b = 'B a segunda letra do alfabeto'
c = 1.1
formato='a={}b={} c={:.2f}'.format(a,b,c)# metodo format argumento passando metodo format

formato='a={0}b={1} c={2:.2f}'.format(a,b,c)

formato='a={nome1}b={nome2} c={nome3:.2f}'.format(nome1=a,nome2=b,nome3=c)
#passando parametro no metodo String

print(formato)
print(formato)
print(formato)