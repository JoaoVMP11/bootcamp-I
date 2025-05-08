soma=0
ct=0
maior_nota=-999999999999999999999999
menor_nota=9999999999999999999999999
ct_aprov=0
qtd=int(input('digite a quantidade de alunos '))
for i in range(1,qtd+1):
    ct += 1
    n=float(input(f'digite a nota do aluno {ct}:'))
    soma+=n
    if maior_nota<n:
        maior_nota=n
    if menor_nota>n:
        menor_nota=n
    if n>=5:
        ct_aprov+=1

print(f'media dos alunos: {(soma/ct):.2f}')
print('maior nota da turma:', maior_nota)
print('menor nota da turma:', menor_nota)
print('quantidade de alunos aprovados:', ct_aprov)


