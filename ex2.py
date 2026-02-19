
tamanho = int(input("Digite o tamanho (altura/largura) da figura (máx 20): "))

if 1 <= tamanho <= 20:
    
    print("\n--- Retângulo Completo ---")
    for i in range(tamanho):
        print("* " * tamanho)

   
    print("\n--- Diagonal Superior Direita ---")
    for i in range(tamanho):
        espacos = "  " * i
        asteriscos = "* " * (tamanho - i)
        print(espacos + asteriscos)
        
else:
    print("Erro: O valor deve estar entre 1 e 20.")