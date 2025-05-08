import random
ct1=0
ct2=0
ct3=0
ct4=0
ct5=0
ct6=0
soma=0

for i in range(1,61):
    n=random.randint(1,6)
    print(n)
    soma+=n
    if n==1:
        ct1+=1
    elif n==2:
        ct2+=1
    elif n==3:
        ct3+=1
    elif n==4:
        ct4+=1
    elif n==5:
        ct5+=1
    else:
        ct6+=1
print('soma ', soma)
print(f'porcentagem de números 1 no sorteio: {(ct1/60)*100}%')
print(f'porcentagem de números 2 no sorteio: {(ct2/60)*100}%')
print(f'porcentagem de números 3 no sorteio: {(ct3/60)*100}%')
print(f'porcentagem de números 4 no sorteio: {(ct4/60)*100}%')
print(f'porcentagem de números 5 no sorteio: {(ct5/60)*100}%')
print(f'porcentagem de números 6 no sorteio: {(ct6/60)*100}%')