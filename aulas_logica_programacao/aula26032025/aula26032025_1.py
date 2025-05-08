ct=0
soma=0
print('digite -1 para sair ')

while True:
    n1=float(input())
    if n1==-1:
        break
    ct=ct+1
    soma=soma+n1
print(f'numero de numeros digitados:{ct}')
print('soma', soma)