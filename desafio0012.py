produto = float(input('Qual o valor do  produto? R$'))
desconto = float(produto*0.05)
vf = float(produto-desconto)
print('O valor do produto com desconto de 5% é de {:.2f}'.format(vf))
