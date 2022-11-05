from random import randint
# 1-Pedra / 2-Papel / 3-Tesoura

traducao = {
  '1': 'Pedra', 
  '2': 'Papel', 
  '3': 'Tesoura'}

tabelaVitoria = {
  'Pedra': 'Tesoura', 
  'Papel': 'Pedra', 
  'Tesoura': 'Papel'
}


def inicio():
  print('=================================')
  print('===== Pedra Papel e Tesoura =====')
  print('=================================')

  print('\nDigite: \n[1] Jogar\n[0] Sair')

  escolha = input('')

  if escolha == '1':
    return jogo()
  else:
    return sair()


def jogo():
  print('\nDigite: \n[1] Pedra\n[2] Papel\n[3] Tesoura')

  escolhaJogador = input('')
  escolhaComputador = str(randint(1, 3))

  # Traducao de numero para Pedra Papel ou Tesoura
  escolhaJogador = traducao[escolhaJogador]
  escolhaComputador = traducao[escolhaComputador]

  # Teste de vitoria
  if escolhaJogador == escolhaComputador:
    print('Empate!')
  elif tabelaVitoria[escolhaJogador] == escolhaComputador:
    print('Você venceu!')
  else:
    print('Você perdeu!')
    
  print(f'Você escolheu {escolhaJogador}')
  print(f'O seu oponente escolheu {escolhaComputador}\n')

  return jogarNovamente()


def jogarNovamente():
  escolha = input('Deseja jogar novamente? (S/N)').upper()

  if escolha == 'S':
    return jogo()
  else:
    return sair()


def sair():
  print('Obrigado por jogar!')
  return


inicio()
