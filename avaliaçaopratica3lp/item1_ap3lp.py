ct=0
soma=0

while True:
    n=float(input("-1 para sair "))
    if n==-1:
        break
    ct= ct+1
    soma=soma+n
print(f'quantidade de valores digitados: {ct}')
print(f'soma de valores digitados: {soma}')
print(f'media de valores digitados: {soma/ct:}')