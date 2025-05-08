def soma_f (valor_1, valor_2):
    soma = valor_1 + valor_2
    return soma
def retorna_soma2(valor_3, valor_4):
    return valor_3 + valor_4
def mostra_soma(valor_5, valor_6):
    print(valor_5+valor_6)
if __name__ == '__main__':
    print(soma_f(float(input('digite um valor ')),float(input('digite outro valor'))))
    print(soma_f(2.1, 3.3))
    print(retorna_soma2(3.1, 4.2))
    mostra_soma(4,9)
    print(mostra_soma(3.1, 4.2))