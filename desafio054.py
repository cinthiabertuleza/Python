from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pessoas in range(1,8):
    nasc = int(input('em que ano a {}ª pessoa nasceu? '.format(pessoas)))
    idade = atual - nasc
    if idade >= 21: #Considerando maioridade aos 21
        totmaior += 1
    else:
        totmenor +=1
print('Ao todo tivemos {} pessoas maiores de idade'. format(totmaior))
print('e {} pessoas menores de idade.'.format(totmenor))
