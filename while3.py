
# Faça um programa que leia o sexo de uma pessoa.
#Mas só aceite os valores 'M' ou 'F'. Caso esteja errado,
#peça a digitação novamente até ter um valor correto.

sexo = str(input('informe seu sexo: [M/F]')).strip().upper()[0]
print(sexo)

while sexo not in 'MnFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))
