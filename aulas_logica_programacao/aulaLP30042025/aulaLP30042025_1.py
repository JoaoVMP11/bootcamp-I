def mostrar_valor (p_valor):
    print(p_valor)
def mostrar_dois_valores (p_valor1, p_valor2):
    print(f'{p_valor1}\n{p_valor2}')

if __name__ == '__main__':
    mostrar_valor(5)
    mostrar_valor(45.6)
    mostrar_valor(-55)

    x=3
    y=3.21
    z=-23.4

    mostrar_valor(x)
    mostrar_valor(y)
    mostrar_valor(z)

    mostrar_valor(float(input('Digite um valor: ')))
    mostrar_valor(float(input('Digite um valor: ')))
    mostrar_valor(float(input('Digite um valor: ')))

    mostrar_dois_valores(6, 9)