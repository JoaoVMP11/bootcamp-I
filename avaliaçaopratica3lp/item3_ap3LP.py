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

if ct_par==0 and ct_impar==0:
    print('impossível obter média dos numeros pares ou impares')
elif ct_par==0:
    print('impossível obter média dos numeros pares')
    print(f'média dos numeros impares: {soma_impar / ct_impar}')
elif ct_impar==0:
    print(f'média dos numeros pares: {soma_par / ct_par}')
    print('impossivel obter média dos numeros impares')
else:
    print(f'média dos numeros pares: {soma_par / ct_par}')
    print(f'média dos numeros impares: {soma_impar / ct_impar}')