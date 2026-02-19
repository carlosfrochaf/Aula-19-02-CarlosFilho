def verificar_equilibrio(expressao):
    stack = []
    mapeamento = {")": "(", "]": "[", "}": "{", ">": "<"}
    
    
    delimitadores = "()[]{}"

    for char in expressao:
        if char in mapeamento.values():  
            stack.append(char)
        elif char in mapeamento:  
            if not stack or stack.pop() != mapeamento[char]:
                return False
    
    return not stack


expressao_usuario = input("Por favor, insira a equação matemática para verificar o equilíbrio: ")
print(f"Expressão '{expressao_usuario}': {verificar_equilibrio(expressao_usuario)}")