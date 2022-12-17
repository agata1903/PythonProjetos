from random import randint
print('-='*10,'Vamos jogar Jo-Ken-Pô!','-='*10)
itens = ('Pedra','Papel','Tesoura')
ia = randint(0,2)
player = int(input('Qual a sua jogada?'))
print('JO')
print('KEN')
print('PÔ')
print('-='*10)
print('IA escolheu ',itens[ia])
print('Player escolheu ',itens[player])
print('-='*10)
if player == 0 and ia == 0:
    print('Empate!')
if player == 0 and ia == 1:
    print('Ah, você perdeu!')
elif player == 1 and ia == 2:
    print('Ah, você perdeu!')
elif player == 2 and ia == 0:
    print('Ah, você perdeu!')
if player == 0 and ia == 2:
    print('Parabéns, você ganhou!')
elif player == 1 and ia == 0:
    print('Parabéns, você ganhou!')
elif player == 2 and ia == 1:
    print('Parabéns, você ganhou!')