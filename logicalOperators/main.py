age = int(input("Digite a tua idade:"))

if age >= 0 and age < 18:
    print("A idade mínima para poder registrar-se no sistema é 18")
elif age < 0 or age > 120:
    print(str(age)+" é a tua idade ? Fala sério :D")
elif age >= 18 and age < 120:
    print("Conta registrada com sucesso")