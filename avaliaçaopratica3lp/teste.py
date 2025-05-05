ct_par=0
soma_par=0
soma_impar=0
ct_impar=0
while True:
    n=float(input('digite um número ou 0 para sair: '))
    if n==0:
        break
    if n%2==0:
        ct_par=ct_par+1
        soma_par=soma_par+n
    else:
        ct_impar=ct_impar+1
        soma_impar=soma_impar+n

print(f'média dos numeros impares: {soma_impar / ct_impar}')
print(f'média dos numeros pares: {soma_par / ct_par}')
