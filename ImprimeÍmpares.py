soma = 0
cont = 0
print('''Aqui está a soma de todos os números ÍMPARES que são
múltiplos de 3, entre o intervalo de 1 até 500:''')
print('')
for impar in range (1,501,2):
    if impar % 3 == 0:
        cont += 1
        soma += impar
print('A soma de todos os {} números solicitados é de {}.'.format(cont, soma))

