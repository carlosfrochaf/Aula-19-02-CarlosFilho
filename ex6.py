def simular_fechadura(entrada_usuario):
    # O delimitador '-' é removido para facilitar a varredura
    sequencia = entrada_usuario.split('-')
    estado = 0

    for digito in sequencia:
        match estado:
            case 0:
                if digito == "1":
                    estado = 1
                else:
                    estado = 0
            case 1:
                if digito == "2":
                    estado = 2
                else:
                    # Se errar o segundo, volta ao início ou verifica se é '1' de novo
                    estado = 1 if digito == "1" else 0
            case 2:
                if digito == "3":
                    estado = 3
                else:
                    estado = 1 if digito == "1" else 0

    if estado == 3:
        print(f"Estado Final: {estado} -> Acesso concedido!")
    else:
        print(f"Estado Final: {estado} -> Acesso negado.")

# Testes
senha_input = input("Digite a senha (ex: 1-2-3): ")
simular_fechadura(senha_input)