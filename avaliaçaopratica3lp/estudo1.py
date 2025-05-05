maior_vlr=-999999999999999999999999
menor_vlr=99999999999999999999999999999999
ct=0

while True:
    n=int(input('digite um numero: '))
    if n==0:
        break
    ct+=1
    if n>maior_vlr:
        maior_vlr=n
    if n<menor_vlr:
        menor_vlr=n
print('maior valor',maior_vlr)
print('menor valor',menor_vlr)
print('ct =',ct)