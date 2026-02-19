
altura = int(input("Digite a altura do triângulo (máx 20): "))


if 1 <= altura <= 20:
    for i in range(1, altura + 1):
        
        print("* " * i)
else:
    print("Erro: A altura deve estar entre 1 e 20.")