'''Drie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostra quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''

contador = soma = 0

while True:
    numero = int(input('Digite um número (o número 999 encerra o programa): '))
    if numero == 999:
        break
    soma += numero
    contador += 1
print(f'Você digitou {contador} números e a soma entre eles é {soma}')

