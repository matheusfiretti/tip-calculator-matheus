print('Bem vindo ao calculador de gorjeta')
total = float(input('Qual o total da conta? $'))
perc = int(input('Quanto gostaria de dar de gorjeta? 10, 12 ou 15? '))
pessoas = int(input('Quantas pessoas vão dividir a conta? '))

total_pessoa = (total * (1 + perc/100)) / pessoas

print(f'O total por pessoa é $ {round(total_pessoa, 2)}')