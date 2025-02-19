aprovados = 0
reprovados = 0
exame = 0
aluno = 0


for notas in range(6):
  for alunos in range(6):
    if aluno< 6:
      aluno = aluno +1
      print("aluno",aluno)
      nota1 = float(input("Digite a primeira nota: "))
      nota2 = float(input("Digite a segunda nota: "))
      media = (nota1 + nota2) / 2
      print(f'A média do aluno {aluno} é : {media}')
      if media > 7:
        print("Aprovado")
        aprovados += 1
      elif media <=2.9:
        print("Reprovado")
        reprovados += 1
      if media >= 3 and media <7:
        print("Exame")
        exame += 1


print(f'O total de alunos aprovados é: {aprovados}')
print(f'O total de alunos reprovados é: {reprovados}')
print(f'O total de alunos em exame é: {exame}')