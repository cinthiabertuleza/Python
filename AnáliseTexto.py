n = (input('Digite algo:'))
#Mostrar o número primitivo e todas as informações possíveis
print('O tipo primitivo desse valor é',type(n))
print('Só tem espaços?',n.isspace())
print('É um número?',n.isnumeric())
print('É ALfabético?', n.isalpha())
print('É Alfanumérico?',n.isalnum())
print('Está maiúsculo?',n.isupper())
print('Está minúsculo?',n.islower())
print('Está capitalizada?',n.istitle())


