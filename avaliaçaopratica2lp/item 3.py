n1=float(input("digite um numero"))
n2=float(input("digite outro numero"))
n3=float(input("digite outro numero"))

if n1>=n2>=n3 or n1>=n3>=n2:
    print('maior numero: ', n1)
elif n2>=n1>=n3 or n2>=n3>=n1:
    print('maior numero: ', n2)
else:
    print('maior numero: ', n3)



