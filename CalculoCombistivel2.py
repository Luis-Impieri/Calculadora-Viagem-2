combustivel = input('Qual o tipo de combustível que o seu veículo usa?')
distancia = float(input('O quão longe é o seu destino em KM?'))

if combustivel == "etanol":
  etanol = 5.8
  quilometragem = 4
  A = (distancia / quilometragem)
  B = (A * etanol)
  print('O valor gasto com combustível na sua viagem será de: ',B,' reais')
elif combustivel == "gasolina":
  gasolina = 5.3
  quilometragem = 3
  A = (distancia / quilometragem) 
  B = (A * gasolina)
  print('O valor gasto com combustível na sua viagem será de: ',B,' reais')
else:
  print('Escolha um combustível válido')
