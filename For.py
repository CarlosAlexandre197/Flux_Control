'''No exemplo iremos percorrer uma lista de chamada de uma determinada escola e contar quantos alunos estão presentes na aula'''

alunos = ['+55 61 8454-6713 'Alexandre', 'ALICE', 'Timoteo', 'Helena', 'tiago', 'SOLANGE']

alunos_presentes = 0

for aluno in alunos:
    print(f'{aluno.title()} presente!')
    alunos_presentes +=1
    
print(f'Alunos presentes: {alunos_presentes}')
    


'''Iremos utilizar a função range para gerarmos alguns números e imprimi-los no terminal:'''

for i in range(10):
    print(i + 1)


'''Funçao range com interrupção do loop'''

for numero in range(1000):
  if numero % 2 != 0:
    continue

  print(f'O número {numero} é par!')

  if numero == 100:
    print('OPS... já verifiquei muitos números pares!')
    break


'''Também podemos utilizar em um FOR loop coleções que retornam mais de um valor.'''

coordenadas = [
  (1, 1, 6),
  (2, 1, 5),
  (3, 4, 4)
]

for x, y, z in coordenadas:
  print(f'x: {x} | y: {y} | z: {z}')