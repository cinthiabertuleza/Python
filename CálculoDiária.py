kms = float(input('Quantos kms foram percorridos?'))
dias = int(input('Quantos dias ficou com o carro?'))
diaria = dias * 60
rodagem = kms * 0.15
total = float(diaria+rodagem)
print('O valor a pagar é de R$ {:.2f}'.format(total))
