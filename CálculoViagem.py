d = float(input('Qual a distância que será percorrida em km? '))
if d <=200:
    v = d*0.5
    print('Você pagará R$ {:.2f} por uma viagem de {} kms.'.format(v,d))
else:
    v = d*0.45
    print('Você pagará R$ {:.2f} por uma viagem de {} kms.'.format(v,d))
