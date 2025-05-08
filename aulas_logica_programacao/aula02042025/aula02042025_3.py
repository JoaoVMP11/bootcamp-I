ct_fem=0
ct_masc=0
maior_altura=-99999999999999999999999999999999999999999999999999999
menor_altura=999999999999999999999999999999999999999999999999999999

while True:
    sexo=input('Digite o sexo [M/F] ou 0 para sair: ')
    if sexo=="0":
        break
    if sexo != "M" and sexo != "F":
            print('erro: digite apenas M ou F')
    altura=float(input('Digite a altura em metros: '))
    if sexo=='M':
        ct_masc+=1
    elif sexo=='F':
        ct_fem+=1
    if altura<menor_altura:
        menor_altura=altura
    if altura>maior_altura:
        maior_altura=altura
print(f'maior altura: {maior_altura}')
print(f'menor altura: {menor_altura}')
print(f'quantidade de pessoas do sexo masculino: {ct_masc}')
print(f'quantidade de pessoas do sexo feminino: {ct_fem}')
