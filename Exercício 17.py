primeiro = int(input("Digite o primeiro número: "))
segundo = int(input("Digite o segundo número: "))

for i in range(primeiro,segundo + 1):
    if i % 2 == 1 :
      print(f'os numeros impares são:  {i}')

