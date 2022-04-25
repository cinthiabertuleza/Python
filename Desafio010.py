real = float(input('Qual o valor que você tem em reais? R$'))
cotacao = float(input('Qual a cotação do dólar?'))
conversao = real/cotacao
dolar = print('Você pode comprar US${:.2f}'.format(conversao),'dólares.')