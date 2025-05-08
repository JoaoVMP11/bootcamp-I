venda=float(input('Valor da venda: '))
compra=float(input('Valor do compra: '))

if venda>compra:
    print(f"teve lucro de: {(venda-compra):.2f}")
elif venda<compra:
    print(f"teve prejuízo de: {(compra-venda):.2f}")
else:
    print('os valores são iguais')
