name = "Qual é o seu nome"
height = input('Qual é o seu pesso? ')
Weight = input('Qual é a sua altura? ')

float_height = float(height)
float_Weight = float(Weight)

imc = float_Weight / float_height ** 2
result = f'{name} tem um imc de {imc:.2f}'
print(result)