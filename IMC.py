peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('E qual é a sua altura? (m) '))
imc = peso/(altura**2)
from time import sleep
print('*=*='*15)
print('\033[0;34mCALCULANDO...\033[m')
sleep(2)
print('*=*='*15)
print('\033[1;36;4mSendo o seu peso {:.2f} kg(s) e a sua altura, {:.2f} metro(s), conclui-se que:\033[m' .format(peso,altura))
print('O seu IMC é {:.2f}.'.format(imc))
if imc < 18.5:
    print('\033[1;33mATENÇÃO!\033[m Você está abaixo do peso e deve se alimentar melhor.'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Você está dentro do peso ideal.\033[1;32m PARABÉNS! =D\033[m'.format(imc))
elif imc >= 25.1 and imc < 30:
    print('\033[1;31mATENÇÃO!\033[m Você está com sobrepeso. Procure ajuda médica.'.format(imc))
elif imc >= 30.1 and imc < 40:
    print('\033[1;31mCUIDADO!\033[m Com esse peso você é considerado obeso e precisa modificar suas rotinas alimentares.'.format(imc))
elif imc > 40:
    print('\033[1;30;41mMUITO CUIDADO!!!\033[m Você está dentro da faixa de Obesidade mórbida e precisa \033[1;31mURGENTE\033[m procurar ajuda médica.'.format(imc))

