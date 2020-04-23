print('Bem vindo Ze Pequeno!!!')

# leitura e conversao
temp_celsius = input('Informe a temperatura: ')
print(type(temp_celsius))
temp_celsius = float(temp_celsius)
print(type(temp_celsius))

# transformacao
temp_farenheit = (temp_celsius * 1.8) + 32
print('A temperatura ' + str(temp_celsius) + ' em celsius equivale a ' + str(temp_farenheit))
