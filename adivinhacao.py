from random import randint

pc = randint(0,10)
cont = 0
acertou = False
while not acertou:
    voce = int(input('Em que número estou pensando? '))
    if voce == pc:
        acertou = True
    else:
        print('Tente novamente!')
    if acertou == False:
        cont += 1
        if cont == 5:
            print('Ah, você perdeu!')
print('Parabéns, você acertou!')

