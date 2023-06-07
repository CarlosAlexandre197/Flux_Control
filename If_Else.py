'''Ao ler a idade de um usuário será impresso na tela se ele é maior ou menor de idade!'''

idade = int(input('Qual é a idade do usuário? '))

if idade >= 18:
    print('usuário é maior de idade!')
else:
    print('usuário é menor de idade!')


'''Velocidade do veículo!'''

velocidade = int(input('Qual é a velocidade do seu veículo? '))

if velocidade < 40:
    print('A sua velocidade está baixa!')
elif velocidade < 100:
    print('A sua velocidade está moderada!')
else:
    print('Cuidado! a sua velocidade está alta.')
    