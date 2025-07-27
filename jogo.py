from random import randint
print('******JOGO DO NÚMERO SECRETO******')

nome = input('\nOlá! Tudo bem? Digite seu nome ao lado ^^ -> ')
print('\n')
print(f'Seja muito bem vindo(a) {nome.title()}! Vamos jogar um jogo?')
print('Bom... O jogo consiste em você tentar adivinhar um número secreto no intervalo de 1 à 20.')
print('Vamos lá!')
x = randint(1,20)
print('\n')
print('Gerando nosso número secreto...')
print('\n')
for tentativa in range(1,4):
  try:
    alternativa = int(input(f'\nPalpite {tentativa}/3 ao número secreto: '))
    print('\n')
  except ValueError:
    print('\nVocê não digitou um número, tente novamente.')
  else:
    if alternativa<=0 or alternativa>=20:
      print(f'{alternativa} está fora do intervalo de 1 à 20.')
    elif alternativa<x:
      print(f'Palpite errado, {alternativa} é menor que o número secreto.')
    elif alternativa>x:
      print(f'Palpite errado, {alternativa} é maior que o número secreto.')
    elif alternativa==x:
      print(f'Parabéns {nome.title()}! Você acertou e o número secreto é {alternativa} ^^')
      break
    else:
      print(f'Sinto muito {nome.title()}, o número secreto não era {alternativa}.')
      print('\n')
if alternativa!=x:
  print(f'O número secreto era {x}.')

print('Saindo...') 
    
    
    

