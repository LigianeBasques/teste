
soma =0
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    soma = soma + num
print('A soma dos valores foi {}!'.format(soma))
