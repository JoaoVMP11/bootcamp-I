a=float(input("digite o comprimento da reta a "))
b=float(input("digite o comprimento da reta b "))
c=float(input("digite o comprimento da reta c "))

if a<=0 or b<=0 or c<=0:
    print("valor invalido")
else:
    if a>=b+c or b>=a+c or c>=b+a:
        print('não é um triangulo')
    else:
        if a!=b and b!=c and a!=c:
            print('é um triangulo escaleno')
        elif (a==b and b!=c and a!=c) or (a==c and b!=c and a!=b) or (a!=b and a!=c and b==c ):
            print('é um triangulo isosceles')
        else:
            print('é um triangulo equilatero')