ct=0
v_inicial=int(input("Digite o valor inicial: "))
v_fim=int(input("Digite o valor fim: "))

if v_fim < v_inicial:
    for i in range(v_inicial,v_fim-1,-1):
        print(i)
        ct+=1
    print('ordem decrescente')
elif v_fim > v_inicial:
    for i in range(v_inicial,v_fim+1):
        print(i)
        ct += 1
    print('ordem crescente')
else:
    print(v_fim)
    print('valores iguais')
    ct+=1
print('total de números:', ct)