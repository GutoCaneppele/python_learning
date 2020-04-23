def Kelvin_to_Celsius(Kelvin):

	return (Kelvin - 273)

def Kelvin_to_Fahrenheit(Kelvin):

	return ((Kelvin - 273) * 9/5) + 32

def Celsius_to_Kelvin(Celsius):

	return (Celsius + 273) 

def Celsius_to_Fahrenheit(Celsius):

	return (Celsius * 9/5) + 32

def Fahrenheit_to_Kelvin(Fahrenheit):
	
	return ((Fahrenheit - 32 ) * 5/9 ) + 273

def Fahrenheit_to_Celsius(Fahrenheit):

	return ((Fahrenheit - 32) * 5/9)
	

if __name__ == '__main__':

	print('Bem vindo!')

	unidade_entrada = input('unidade inicial (C, F ou K):')
	unidade_final = input('unidade_final (C, F, ou K):')
	temp_entrada_str = input('temperatura incial:')
	temp_entrada_str.replace(' ', '')
	temp_entrada = float(temp_entrada_str)

	resultado = None

	if unidade_entrada == 'K' and unidade_final == 'C': 
		resultado = Kelvin_to_Celsius(temp_entrada) # para transformação de Kelvin para Celsius;

	elif unidade_entrada == 'K' and unidade_final == 'F':
		resultado = Kelvin_to_Fahrenheit(temp_entrada) # para transformação de Kelvin para Fahrenheit;


	elif unidade_entrada == 'C' and unidade_final == 'K': # para transformação de Kelvin para Celsius;
		resultado = Celsius_to_Kelvin(temp_entrada)

	elif unidade_entrada == 'C' and unidade_final == 'F': # para transformação de Celsius para Fahrenheit;
		resultado = Celsius_to_Fahrenheit(temp_entrada)


	elif unidade_entrada == 'F' and unidade_final == 'K':
		resultado = Fahrenheit_to_Kelvin(temp_entrada) # para tranformação de Fahrenheit para Kelvin;

	elif unidade_entrada == 'F' and unidade_final == 'C':
		resultado = Fahrenheit_to_Celsius(temp_entrada) # para transformação de Fahrenheit para Celsius;

	if resultado is None:
		print('Error')

	msg_resultado = 'Temperatura final: {}{}'.format(resultado, unidade_final)

	print(msg_resultado)
