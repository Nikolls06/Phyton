while True:
    base = float(input('Digite o base do triângulo: '))
    altura = float(input('Digite o altura lado do triângulo: '))

    area = (base * altura) / 2
    print('a área do triângulo é: ',area)

    resposta = str(input('Quer continuar (s/n)')).strip().lower()
    if resposta == 'n':
        print('Programa interrompido')
        break


