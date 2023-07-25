#Vamos fazer um jogo do bingo em Python.
#Faremos um aplicativo sem interface gráfica usando apenas caractéres do teclado do computador

#*****************************************************************************************************************************
#
#
#
#0:Importando as bibliotecas usadas

import random
import time


#*****************************************************************************************************************************
#
#
#
#1:Cabeçalho do jogo e instruções de uso
print('\n')
print('\n')
print('\033[01m'+'$$$$   $$$$   $       $    $           $  $    $      $  $$$$$      $$$$')
print('\033[01m'+'$   $  $      $ $   $ $     $         $   $    $ $    $  $    $    $    $')
print('\033[01m'+'$    $ $      $  $ $  $      $       $    $    $  $   $  $     $  $      $')
print('\033[01m'+'$$$$$  $$$$   $   $   $       $     $     $    $   $  $  $     $  $      $')
print('\033[01m'+'$    $ $      $       $        $   $      $    $    $ $  $     $  $      $') 
print('\033[01m'+'$   $  $      $       $         $ $       $    $     $$  $    $    $    $')
print('\033[01m'+'$$$$   $$$$$  $       $          $        $    $      $  $$$$$      $$$$  \n\n')

print('Seja bem vindo ao jogo do bingo feito em Python!!!\nEsperamos que você se divirta.\nNo jogo de bingo números de 1 a 90 serão sorteados e quem completar a cartela primeiro assinalando todo os números será o campeão da rodada.\nOs números serão sorteados usando um gerador de números aleatórios.\nA CPU terá seu próprio jogador, mas você poderá incluir quantos jogadores você quiser.\nCada jogador será indentificado por seu nome e terá uma cartela contendo números de 01 a 90.\nAo ser solicitado você deve inserir informação de acordo com a solicitação feita.\nErros na inserção de dados podem ocasionar erros no desenrolar do jogo.\n')


#***********************************************************************************************************************************************************************************************
#
#
#
#2:Funções úteis durante a realização do jogo

def numero_string(n:int)->str:
 '''Função que converte número inteiro em um string com dois digitos'''
 string:str=str(n).zfill(2)
 return string

def highlight(string:str)->str:
 '''Função para marcar uma string'''
 return('\033[31m'+'\033[01m'+string+'\033[0;0m')


#***********************************************************************************************************************************************************************************************
#
#
#
#3:Definindo a classe de jogador e criando os jogadores da rodada de bingo

class jogador(object):
 #Vamos intanciar os atributos da classe
 def __init__(self, nome:str, acertos:int):
  '''Instanciando os atributos da classe jogador'''
  self.nome=nome
  self.acertos=acertos
  self.cartela=[] #atributo inicializado como uma lista vazia

 #Métodos da classe
 def criar_cartela(self):
  '''Função usada para criar uma cartela'''
  for i in range(15):
   self.cartela.append(numero_string(random.randint(1,90)))
   self.cartela=self.cartela
  return self.cartela

 def exibir_cartela(self):
  '''Função que exibe a cartela e mostra o status do jogador'''
  print(' ')
  print('Jogador {} eis a sua cartela: '.format(self.nome))
  print('+------+------+------+------+------+ ')
  print('|      |      |      |      |      | ')
  print('|  {}  |  {}  |  {}  |  {}  |  {}  | '.format(self.cartela[0], self.cartela[3], self.cartela[6], self.cartela[9], self.cartela[12]))
  print('|      |      |      |      |      | ')
  print('+------+------+------+------+------+ ')  
  print('|      |      |      |      |      | ')
  print('|  {}  |  {}  |  {}  |  {}  |  {}  | '.format(self.cartela[1], self.cartela[4], self.cartela[7], self.cartela[10], self.cartela[13]))
  print('|      |      |      |      |      | ')
  print('+------+------+------+------+------+ ')  
  print('|      |      |      |      |      | ')
  print('|  {}  |  {}  |  {}  |  {}  |  {}  | '.format(self.cartela[2], self.cartela[5], self.cartela[8], self.cartela[11], self.cartela[14]))
  print('|      |      |      |      |      | ')
  print('+------+------+------+------+------+ ')  

 def atualizar_acertos(self, n:str):
  '''Função que contabiliza o número de acertos de cada jogador'''
  for i in range(15):
   if(n==self.cartela[i]):
    self.cartela[i]=highlight(self.cartela[i])
    self.acertos=self.acertos+1
  if(self.acertos==15):
   print('\033[34m'+'\033[01m'+'$$$$   $  $   $   $$$   $$$$'+'\033[0;0m')
   print('\033[34m'+'\033[01m'+'$   $  $  $$  $  $     $    $'+'\033[0;0m')
   print('\033[34m'+'\033[01m'+'$$$$   $  $ $ $  $ $$  $    $'+'\033[0;0m')
   print('\033[34m'+'\033[01m'+'$   $  $  $  $$  $   $ $    $'+'\033[0;0m')
   print('\033[34m'+'\033[01m'+'$$$$   $  $   $   $$$$  $$$$'+'\033[0;0m')
  return self.acertos



#***********************************************************************************************************************************************************************************************
#
#
#
#3:Criando os jogadores 

#Criando uma lista de jogadores
players:list=[]

#Definindo o jogador da máquina
cpu=jogador("CPU", 0)
cpu.criar_cartela()
players.append(cpu)


#Definindo jogadores manualmente
numero_jogadores:int=int(input('Quantos jogadores você deseja criar? '))

#Instanciando os jogadores
for i in range(numero_jogadores):
 a:str=str(input('Jogador digite o seu nome: '))
 player=jogador(a,0)
 player.criar_cartela()
 players.append(player)

#Atualizando a lista de jogadores
players= players
#Exibindo a cartela do jogadores
for i in range(len(players)):
 players[i].exibir_cartela()

#**********************************************************************************************************************************************************************************************
#
#
#
#4: Rodando o jogo

#Criando uma variável para ir alocando os números sorteandos
numeros_sorteados:list = ['01','02','03','04','05','06','07','08','09','10','11','12','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59', '60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90']
contador:int=0 #Variável usada para se contar
status1:bool=False #variável usada para encerrar o jogo
status2:bool=False #variável usada para definir se a escolha de número é válida
#Introdução
print('Preparados?!\nVamos começar a sortear os números.\nAperte a tecla enter para que um número seja sorteado')

#Vamos rodar um loop while para definir o o rumo do jogo
while(status1==False): #Loop principal

 #Sorteando um número
 stop=input()
 numero_da_rodada:str=str(random.choice(numeros_sorteados))
 contador=contador+1
 numeros_sorteados.remove(numero_da_rodada)
 print('O número sorteado é {}'.format(highlight(numero_da_rodada)))
 #Atualizando os status do jogadores
 for j in range(len(players)):
  players[j].atualizar_acertos(numero_da_rodada)
  players[j].exibir_cartela()


 #Resentando o valor da variável de checagem do número sorteado e a variável alocando os números sorteados
 status2=False
 numeros_sorteados=numeros_sorteados

 #Checando se  fim do jogo foi alcaçando
 for j in range(len(players)):
  if(players[j].acertos==15):
   status1=True
   break
  else:
   status1=False
  

#***********************************************************************************************************************************************************************************************
#
#
#
#5:Encerramento do jogo
print('\033[94m'+'\033[01m'+'Esperamos que tenha se divertido!!!')
print(' ')
print(' ')
print('\033[94m'+'\033[01m'+' ***   ****   ****    *   ***       *      ****    ***     *  *  *')
print('\033[94m'+'\033[01m'+'*   *  *   *  *   *   *  *   *     * *     *   *  *   *    *  *  *')
print('\033[94m'+'\033[01m'+'*   *  ****   ****    *  *        *****    *   *  *   *    *  *  *')
print('\033[94m'+'\033[01m'+'*   *  *   *  *   *   *  * ***   *     *   *   *  *   *           ')
print('\033[94m'+'\033[01m'+' ***   ****   *    *  *   ***   *       *  ****    ***     *  *  *')
print(' ')
print(' ')
print(' ')
print(' ')
quit()










