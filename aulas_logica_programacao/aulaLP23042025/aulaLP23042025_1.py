ct=0
soma=0
v_inicial=int(input('digite o valor inicial '))
v_fim=int(input('digite o valor final '))

for i in range(v_inicial,v_fim+1):
    if i!=v_fim:
        print(i, end=",")
    else:
        print(i)
    ct+=1
    soma+=i
print('total de numeros: ', ct)
print('soma dos números: ', soma)


