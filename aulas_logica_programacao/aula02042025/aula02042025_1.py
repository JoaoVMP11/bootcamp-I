menor_valor=99999999999999999999999999999999999999999999999999999999999999999999999999999
ct=0
soma=0

while True:
    n=int(input('digite um número ou 0 para sair: '))
    if n==0:
        break
    ct+=1
    soma+=n
    if n<menor_valor:
        menor_valor=n
print('menor valor:', menor_valor)
print('numero de valores', ct)
print('soma dos valores', soma)
print(f'média dos valores{soma/ct}')