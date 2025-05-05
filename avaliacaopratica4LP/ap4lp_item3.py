soma=0
ct=0
for i in range(0,11,1):
    ct+=1
    soma+=2*i
    print(2*i)
print('soma: ', soma)
print(f'media: {soma/ct}')