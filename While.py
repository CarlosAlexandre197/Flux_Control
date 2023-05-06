'''Neste exemplo, iremos imprimir uma variável enquanto o valor dela for menor ou igual a 100:'''

valor = 1

while valor <= 100:
    print(f'O valor é: {valor:03}')
    valor += 1


'''Também podemos utilizar as instruções CONTINUE e BREAK dentro de um WHILE.'''

numero = 0

while numero <= 1000:
    if numero % 2 != 0:
        numero += 1
        continue

    print(f'O número: {numero} é par!')

    if numero == 100:
        print('OPS... Já verifiquei muitos número pares!')
        break

    numero += 1