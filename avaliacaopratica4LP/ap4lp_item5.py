ct=0
n= int(input('digite o valor inicial da sequencia de números naturais em ordem decrescente '))
for i in range (n,-1,-1):
    ct+=1
    print(i)
print('total de números: ', ct)