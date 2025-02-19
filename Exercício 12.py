peso = int(input("Digite seu peso "))
altura = float(input("Digite sua altura "))/100
imc = peso / (altura * altura)

if imc < 18:
  print("Magreza")
elif imc < 24.9:
  print("Saudável")
elif imc < 29.9:
  print("Sobrepeso")
else:
  print("Obesidade")

print(imc)