# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0
# com uma pausa de 1 segundo entre eles.

from time import sleep
print('A contagem regressiva irá iniciar!!!')
sleep(1)
for cont in range(10, -1, -1):
    sleep(1)
    print(cont, '!')
sleep(1)
print('LANÇAR!!!')

