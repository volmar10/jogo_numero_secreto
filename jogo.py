from random import randint
print('******JOGO DO NÚMERO SECRETO******')
print('\n')
nome = input('\nOlá! Tudo bem? Digite seu nome ao lado ^^ -> ')
print(f'Seja muito bem vindo(a) {nome.title()}! Vamos jogar um jogo?')
print('Bom... O jogo consiste em você tentar adivinhar um número secreto no intervalo de 1 à 10.')
print('Vamos lá!')
x = randint(1,10)
print('\n')
print('Gerando nosso número secreto...')
print('\n')
for tentativa in range(1,6):
  try:
    alternativa = int(input(f'\nPalpite {tentativa}/5 ao número secreto: '))
    print('\n')
  except ValueError:
    print('\nVocê não digitou um número, tente novamente.')
  else:
    if alternativa<=0 or alternativa>=10:
      print(f'{alternativa} está fora do intervalo de 1 à 10.')
    if alternativa==x:
      print(f'Parabéns {nome.title()}! Você acertou e o número secreto é {alternativa} ^^')
      break
    else:
      print(f'Sinto muito {nome.title()}, o número secreto não era {alternativa}.')
      print('\n')
if alternativa!=x:
  print(f'O número secreto era {x}.')

print('Saindo...') 
    
    
    

