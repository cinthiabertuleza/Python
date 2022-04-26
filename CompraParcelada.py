print('\033[1;35m{:-^40}\033[m'.format(' LOJAS CINTHIA '))
print('')
from time import sleep
sleep(1)
preco = float(input('VALOR DAS COMPRAS: R$ '))
print('''QUAL A FORMA DE PAGAMENTO?
[ 1 ] À VISTA (DINHEIRO)
[ 2 ] À VISTA (CARTÃO)
[ 3 ] EM ATÉ 2X NO CARTÃ0
[ 4 ] EM 3X OU MAIS NO CARTÃO''')
opcao = int(input('QUAL É A OPÇÃO? '))
vistadinheiro = preco - (preco * 0.10)
vistacartao = preco - (preco * 0.05)
if opcao == 1:
    print('Sua compra de {:.2f} terá 10% de desconto.'.format(preco))
    print('Sua compra custará R$ {:.2f}.'.format(vistadinheiro))
    sleep(2)
    print('')
    print('{:^40}'.format(' \033[1;35mAGRADECEMOS A PREFERÊNCIA! '))
    print('{:^40}'.format(' \033[1;35mVOLTE SEMPRE!'))
    print('{:^40}'.format(' \033[1;35m;) '))
elif opcao == 2:
    print('Sua compra de {:.2f} terá 5% de desconto.'.format(preco))
    print('Sua compra custará R$ {:.2f}.'.format(vistacartao))
    sleep(2)
    print('')
    print('{:^40}'.format(' \033[1;35mAGRADECEMOS A PREFERÊNCIA! '))
    print('{:^40}'.format(' \033[1;35mVOLTE SEMPRE!'))
    print('{:^40}'.format(' \033[1;35m;) '))
elif opcao == 3:
    precodividido = preco / 2
    print('Sua compra de R$ {:.2f} será parcelada em 2x.'.format(preco))
    print('Você pagará 2 parcelas de R$ {:.2f}'.format(precodividido))
    sleep(2)
    print('')
    print('{:^40}'.format(' \033[1;35mAGRADECEMOS A PREFERÊNCIA! '))
    print('{:^40}'.format(' \033[1;35mVOLTE SEMPRE!'))
    print('{:^40}'.format(' \033[1;35m;) '))
elif opcao == 4:
    vezes = int(input('EM QUANTAS PARCELAS? '))
    precojuros = (preco + (preco * 0.20)) / vezes
    precofinal = preco + (preco * 0.20)
    print('Sua compra será parcelada em {} vezes de {:.2f} e terá um acréscimo de \033[4m20% de juros\033[m.'.format(vezes,precojuros))
    print('Sua compra vai custar R$ {:.2f} no final.'.format(precofinal))
    sleep(2)
    print('')
    print('{:^40}'.format(' \033[1;35mAGRADECEMOS A PREFERÊNCIA! '))
    print('{:^40}'.format(' \033[1;35mVOLTE SEMPRE!'))
    print('{:^40}'.format(' \033[1;35m;) '))
else:
    print('\033[1;31mOpção Inválida! Escolha uma das opções listadas acima.\033[m')



