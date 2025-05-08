ct=0
soma=0
ct_geral=0

while True:
    n1=float(input('Digite um valor: '))
    if n1==0:
        break
    ct_geral=ct_geral+1
    if n1%2!=1:
        ct=ct+1
        soma=soma+n1

print(f'media dos numeros pares: {(soma/ct):.4f}')
print(f'quantidade de numeros pares {ct}')
print(f'quantidade de numeros digitados {ct_geral}')