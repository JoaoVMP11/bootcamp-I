ano_nascimento=int(input('Digite o ano de nascimento: '))
ano_atual=int(input('Digite o ano atual: '))
nome=input('Digite o nome: ')

idade= ano_atual-ano_nascimento

print('seu nome: ', nome)
print('ano de nascimento:', ano_nascimento)
print('sua idade: ', idade)

if 16 <= idade < 18:
    print('você pode votar')
elif idade>=18:
    print('você pode votar e obter a cnh')
else:
    print('não pode nada')