meses = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]

numeroMes = int(input("Digite o número do mês: "))

if 1 <= numeroMes <= 12:
    print(meses[numeroMes - 1])
else:
    print("Mês inválido")
