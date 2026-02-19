def analisador_lexico(sentenca):
    categorias = {
        "=": "Atribuição",
        "+": "Operador",
        "-": "Operador",
        "*": "Operador",
        "/": "Operador",
        ";": "Fim de instrução"
    }

    
    partes = sentenca.split()

    print(f"Analisando: {sentenca}\n" + "-"*20)

    for item in partes:
        if item in categorias:
            print(f"• {item} -> {categorias[item]}")
        elif item.isdigit():
            print(f"• {item} -> Número")
        elif item.isidentifier():
            print(f"• {item} -> Identificador")
        else:
            print(f"• {item} -> Desconhecido")


soma_exemplo = "soma = 10 + 20 ;"
analisador_lexico(soma_exemplo)