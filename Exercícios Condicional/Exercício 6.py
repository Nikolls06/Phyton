salario = float(input("Digite o valor do seu salário: "))

if salario < 1000:
    aumento1 = salario * 1.25
    print("Seu salário sofreu um aumento de 25% e agora está no valor de: ", aumento1)

elif salario >= 1000 and salario < 2000:
    aumento2 = salario * 1.15
    print("Seu salário sofreu um aumento de 15% e agora está no valor de: ", aumento2)

elif salario >= 2000:
    aumento3 = salario * 1.1
    print("Seu salário sofreu um aumento de 10% e agora está no valor de: ", aumento3)
   