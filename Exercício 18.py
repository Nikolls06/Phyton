primeiro = int(input("Digite o primeiro número: "))
segundo = int(input("Digite o segundo número: "))

somaImpar = 0

for num in range(primeiro,segundo + 1):
    if num % 2 == 1 :
      somaImpar += num
print(f'a soma é:  {somaImpar}')
 