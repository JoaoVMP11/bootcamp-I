ano_nascimento=int(input('Digite o ano de nascimento: '))
ano_atual=int(input('Digite o ano atual: '))
nome=input('Digite o nome: ')

idade= ano_atual-ano_nascimento

print('seu nome: ', nome)
print('ano de nascimento:', ano_nascimento)
print('sua idade: ', idade)

if idade>=16:
    print('você pode votar')
else:
    print('você não pode votar')
