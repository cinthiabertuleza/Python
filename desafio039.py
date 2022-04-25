ano = int(input('Qual o ano do seu nascimento? '))
atraso = (2022 - ano) - 18
faltam = 18 - (2022 - ano)
ideal = (2022 - ano)
print('Você nasceu em {} e tem {} anos em 2022.'.format(ano, 2022-ano))
if faltam > 0:
    print('Você ainda tem prazo de {} ano (s) para se alistar ao serviço militar.'.format(faltam))
elif ideal == 18:
    print('Está na hora de se alistar ao serviço militar')
elif atraso > 0:
    print('Você deveria ter feito o alistamento militar há {} anos.'.format(atraso))