f_inicial=int(input('digite o grau Fahreinheit inicial: '))
f_final=int(input('digite o grau Fahreinheit final: '))

print('Fahreinheit | Celsius')
if f_inicial <= f_final:
    for f in range (f_inicial,f_final+1):
        print(f'{f}ºF |  {(5/9)*(f-32)}ºC')
else:
    for f in range (f_inicial,f_final-1, -1):
        print(f'{f}ºF |  {(5 / 9) * (f - 32)}ºC')


