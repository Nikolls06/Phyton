lanches = ["Big Mac", "Qauarteirão", "McChicken", "Cheddar McMelt", "McMax"]

lache = int(input("Digite o número do lanche desejado: "))
if 1 <= lache <= 5:
  print(lanches[lache - 1])
else:
  print("Lanche inválido") 