from desenho import *
import palavras
import random
aleatorio = random.choice #atribuindo módulo a uma variável
categorias=[aleatorio(palavras.filmes()),aleatorio(palavras.animais()),aleatorio(palavras.desenhos()),aleatorio(palavras.series()),aleatorio(palavras.games())]#Sortea uma categoria aleatória.
newgame = 1
bestname = ''
bestscore = 0
while newgame == 1: # Menu Principal
    jognov = 1
    inicio()
    print('\n1 - Novo jogo\n2 - Sair')
    newgame =  int(input('Selecione uma opção: '))
    if newgame == 1:
       print('1 - Normal\n2 - Blitz')
       tipogame = int(input('Selecione uma opção: '))
       if tipogame == 1:
           vit = der = 0  # Reseta pontos
           nome = input ('Nome do jogador: ')  # Nome do novo jogador
           while jognov == 1 :
               erros = 0  # reseta o número de erros
               # CAPTURA PALAVRA INICIAL
               print ('Qual modo deseja jogar?\n  ')
               print ('1 - Escolher palavra\n2 - Escolher uma categoria\n3 - Sortear uma categoria\n')
               modo = int (input ('Selecione uma opção : '))
               # Escolhe palavra para acertarem.
               if modo == 1 :
                   word = input ('\nInforme a palavra: ');
                   temp = []
                   for letra in word :
                       if letra == ' ' :
                           temp.append (' ')
                       else :
                           temp.append ('_')
                   # Permite o usuário escolher uma categoria.
               elif modo == 2 :
                   print ('1 - Animais\n2 - Filmes\n3 - desenhos/animes\n4 - series\n5 - jogos')
                   print ('\n')
                   categ = int (input ('Selecione uma opção:  '))
                   # Seleciona uma palavra da categoria animais.
                   if categ == 1:
                       word = aleatorio(palavras.animais())
                       temp = []
                       for letra in word:
                           if letra == ' ':
                               temp.append(' ')
                           else:
                               temp.append('_')
                       # Seleciona uma palavra da categoria filmes.
                   elif categ == 2:
                       word = aleatorio(palavras.filmes())
                       temp = []
                       for letra in word:
                           if letra == ' ':
                               temp.append(' ')
                           else:
                               temp.append('_')
                       # Seleciona uma palavra da categoria desenhos/animes
                   elif categ == 3:
                       word = aleatorio(palavras.desenhos())
                       temp = []
                       for letra in word:
                           if letra == ' ':
                               temp.append(' ')
                           else:
                               temp.append('_')
                       # Seleciona uma palavra da categoria seriados
                   elif categ == 4:
                       word = aleatorio(palavras.series())
                       temp = []
                       for letra in word:
                           if letra == ' ':
                               temp.append(' ')
                           else:
                            temp.append('_')
                       # Seleciona uma palavra da categoria games
                   elif categ == 5:
                       word = aleatorio(palavras.games())
                       temp = []
                       for letra in word:
                           if letra == ' ':
                               temp.append(' ')
                           else:
                            temp.append('_')
                   # Sortea uma categoria para jogar.
               elif modo == 3 :
                   categ = aleatorio (categorias)
                   word = categ
                   temp = []
                   for letra in word :
                       if letra == ' ' :
                           temp.append (' ')
                       else :
                           temp.append ('_')

               while True :

                   print ('\n' * 20)  # limpa a tela
                   print ('Jogador: {} | Vitórias: {} | Derrotas: {} | Partidas: {}'.format (nome, vit, der, vit + der))
                   print ()
                   forca (erros, nome, vit, der)  # imprime desenho da forca

                   # imprime a adivinhacao
                   print ('\n\nAdivinhe: ', end='')

                   for let in temp :
                       print (let, end=' ')

                   print ('\n' * 2)

                   # Verifica se perdeu
                   if erros == 6 :
                       der += 1
                       break

                   # Verificar se o jogador ganhou
                   ganhouJogo = True
                   for let in temp :
                       if let == '_' :
                           ganhouJogo = False
                   if ganhouJogo :
                       vit += 1
                       print ('\033[1;32m\nPARABÉNS VENCEDOR!!!\033[m')
                       break

                   # captura a letra do usuario
                   print ('2 - Desistir')
                   letraDig = input ('Informe uma letra:').upper()
                   if letraDig == '2' :
                       der += 1
                       break

                   # verifica se acertou alguma letra
                   errouLetra = True
                   for i, let in enumerate (word) :
                       if word [i] == letraDig :
                           temp [i] = word [i]
                           errouLetra = False
                   if errouLetra :
                       erros = erros + 1
               print ('\nJogador: {} | Vitórias: {} | Derrotas: {} | Partidas: {}'.format (nome, vit, der, vit + der))
               print ('\nDeseja jogar novamente?')
               print ('1 - Continuar jogando  2 - Menu')
               jognov = int (input ('\nSelecione uma opção: '))

        # Modo blitz
       elif tipogame == 2:
           vit = der = 0  # Reseta pontos
           nome = input ('Nome do jogador: ')  # Nome do novo jogador
           while jognov == 1 :
               erros = 0  # reseta o número de erros

               categ = aleatorio (categorias)
               word = categ
               temp = []
               for letra in word :
                   if letra == ' ' :
                       temp.append (' ')
                   else :
                       temp.append ('_')

               while True :
                   # Verifica record
                   arquivo = open('recordescore.txt', 'rt')
                   pontuacao = int(arquivo.read())

                   if vit > pontuacao:
                       bestscore = vit
                       bestname = nome
                       recordename = open('recordename.txt','wt')
                       recordename.write(bestname)
                       recordename.close()
                       recorde = open('recordescore.txt','wt')
                       recorde.write(str(bestscore))
                       recorde.close()
                       arquivo.close()
                   recordename1 = open('recordename.txt','rt')
                   recorde1 = open('recordescore.txt','rt')
                   print ('\n' * 20)  # limpa a tela
                   print ('Jogador: {} | Vitórias: {} | Derrotas: {} | Partidas: {}'.format (nome, vit, der, vit + der))
                   print ('Recorde: Nome: {} | Vitórias: {}'.format(recordename1.read(),recorde1.read()))
                   forca (erros, nome, vit, der)  # imprime desenho da forca
                   recorde1.close()
                   recordename1.close()

                   # imprime a adivinhacao
                   print ('\n\nAdivinhe: ', end='')

                   for let in temp :
                       print (let, end=' ')

                   print ('\n' * 2)

                   # Verifica se perdeu
                   if erros == 6 :
                       der += 1
                       break

                   # Verificar se o jogador ganhou
                   ganhouJogo = True
                   for let in temp :
                       if let == '_' :
                           ganhouJogo = False
                   if ganhouJogo :
                       vit += 1
                       print ('\033[1;32m\nPARABÉNS VENCEDOR!!!\033[m')
                       break



                   # captura a letra do usuario
                   print ('2 - Desistir')
                   letraDig = input ('Informe uma letra:').upper()
                   if letraDig == '2' :
                       der += 1
                       break

                   # verifica se acertou alguma letra
                   errouLetra = True
                   for i, let in enumerate (word) :
                       if word [i] == letraDig :
                           temp [i] = word [i]
                           errouLetra = False
                   if errouLetra :
                       erros = erros + 1
               if der > 0:
                   break

    else:
        break
