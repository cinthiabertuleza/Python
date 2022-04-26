v = float(input('Sua velocidade é: '))
m = (v-80)*7
if v > 80:
    print('Você foi multado, excedeu o limite de 80Kms/h!')
    print('Sua multa será de R${:.2f}'.format(m))
print('Dirija com segurança!')
