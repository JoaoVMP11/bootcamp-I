n1=int(input("digite um numero"))
n2=int(input("digite outro numero"))

print('seus numeros em ordem crescente:')
if n1>=n2:
    print(f'{n2},{n1}')
else:
    print(f'{n1}, {n2}')