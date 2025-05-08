ct=0
soma=0
nome= input('Qual o nome da disciplina? ')
while True:
    n1=float(input('Digite o valor da nota: '))
    if n1==-1:
        break
    ct=ct+1
    soma=(soma+n1)
media= soma/ct
print(f'numero de notas: {ct}')
print(f'media das notas: {media:.2f}')
print(f'soma: {soma}')
print(f'nome da disciplina: {nome}')