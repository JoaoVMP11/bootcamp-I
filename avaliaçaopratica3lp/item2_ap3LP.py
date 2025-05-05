ct_aprov=0
ct_reprov=0

while True:
    nota=float(input("Digite a nota do aluno ou -1 para sair : "))
    if nota==-1:
        break
    if nota>=5:
        ct_aprov=ct_aprov+1
    else:
        ct_reprov=ct_reprov+1
print('alunos aprovados: ',ct_aprov)
print('alunos reprovados: ',ct_reprov)
print(f'total de alunos que fizeram a prova {ct_aprov+ct_reprov}')