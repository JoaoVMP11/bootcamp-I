altura=float(input('digite sua altura em metros'))
sexo=str(input('digite seu sexo ( homem ou mulher): '))

if sexo=='mulher':
    print('peso ideal em kg: ',(62.1*altura)-58)
else:
    print('peso ideal em kg:', (72.7*altura)-44,7)
