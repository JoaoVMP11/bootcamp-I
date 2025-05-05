def idade (ano_nascimento):
    ano_atual=2025
    return ano_atual-ano_nascimento

if __name__ == '__main__':
    age=idade(int(input('escreva o ano de nascimento ')))
    print(age)