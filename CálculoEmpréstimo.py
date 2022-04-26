casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o valor do seu salário? R$ '))
anos = int(input('Em quantos anos pretende pagar o empréstimo? '))
pmt = casa/(anos*12)
print('Para pagar uma casa de R${:.2f} '.format(casa), end='')
print('em {} anos, a prestação será de R$ {:.2f}'.format(anos, pmt))
if pmt > salario*0.30: #True
    print('Lamentamos, mas infelizmente não podemos conceder o empréstimo.')
else:
    print('Parabéns, seu empréstimo foi aprovado!')
