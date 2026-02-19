
conjunto_a = [1, 2, 3]
conjunto_b = [2, 3, 4]


uniao = list(conjunto_a)

for elemento in conjunto_b:
    
    if elemento not in uniao:
        uniao.append(elemento)

# --- OPERAÇÃO DE INTERSEÇÃO ---
intersecao = []

for elemento in conjunto_a:
    
    if elemento in conjunto_b:
        intersecao.append(elemento)


print(f"A = {conjunto_a}, B = {conjunto_b}")
print(f"• União: {uniao}")
print(f"• Interseção: {intersecao}")