rows = int(input("Quantas linhas desejas: "))
colmuns = int(input("Quantas colunas desejas: "))
symbol = input("Digite o simbolo que pretende usar:")

for i in range(rows):
    for j in range(colmuns):
        print(symbol, end="")
    print()