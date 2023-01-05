cont = soma = sub = mult = div = 0
resp = 0
print('Olá, vamos aprender tabuada?')
print('-'*50)
resp = int(input('Qual operação matemética você gostaria de ver a tabuada? \n[1]Soma\n[2]Subtração\n[3]Multiplicação\n[4]Divisão \n').upper())
print('-'*50)
if resp <= 4:
    n = int(input('Digite um número: '))
    while n > 0:
        cont += 1
        if n < 0:
            break
        if resp == 1:
            soma = n + cont
            print(n, '+', cont, '=', soma)
            if cont >= 10:
                break
        elif resp == 2:
            sub = n - cont
            print(n, '-', cont, '=', sub)
            if cont >= 10:
                break
        elif resp == 3:
            mult = n * cont
            print(n, 'x', cont, '=', mult)
            if cont >= 10:
                break
        else:
            div = n / cont
            print(n, '÷', cont, '=', div)
            if cont >= 10:
                break
    print('-' *50)
    print('Fim da tabuada')
print('-'*50)
print('Bons estudos!')
