
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        par = par + 1
    else:
        impar = impar + 1
print('VocÊ digitou {} números pares e {} números ímpares!'.format(par, impar))