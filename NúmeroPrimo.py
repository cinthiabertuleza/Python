num = int(input('Digite um número: ')) #Para saber se um número é primo.
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[35m', end=' ') #primos
        tot += 1
    else:
        print('\033[33m', end=' ') #não primos
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi dividido {} vezes...'.format(num,tot))
if tot == 2:
    print('E por isso ele é primo.')
else:
    print('E por isso ele não é primo.')
