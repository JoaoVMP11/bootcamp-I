n1=float(input("digite um numero "))
operacao=input("digite uma operacao (+ , - , * , / ) ")
n2=float(input("digite outro numero "))

if operacao == '+':
    print(f'{n1+n2}')
elif operacao == '-':
    print(f'{n1-n2}')
elif operacao == '*':
    print(f'{n1*n2}')
elif operacao == '/':
    if n2==0:
        print('jamais dividirás por zero')
    else:
        print(f'{n1 / n2}')

else:
    print('erro. Escolha uma operacao entre as apresentadas')