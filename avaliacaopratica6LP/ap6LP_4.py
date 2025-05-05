#função que calcula o imc do usuário com base nos valores que o mesmo digita.

def calcula_imc (peso, altura):
    imc = peso / (altura ** 2)
    return imc
if __name__ == '__main__':
    print('imc do usuário: ', calcula_imc(float(input('digite o seu peso ')), float(input('digite a sua altura  '))))