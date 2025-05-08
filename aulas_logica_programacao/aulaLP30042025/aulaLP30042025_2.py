def dobro_f(n):
    dobro=2*n
    return dobro

def triplo_f(p_valor):
    triplo=p_valor*3
    return triplo

if __name__ == '__main__':
    valor= float(input('Digite um valor: '))
    print(dobro_f(valor))
    print(triplo_f(valor))
