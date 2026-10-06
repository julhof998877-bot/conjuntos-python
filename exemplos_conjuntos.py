# Exemplos de Conjuntos em Python

# Criando conjuntos
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {4, 5, 6, 7, 8}

print("Conjunto A:", conjunto_a)
print("Conjunto B:", conjunto_b)

# 1. União
# Junta todos os elementos dos dois conjuntos,
# eliminando os elementos repetidos.
uniao = conjunto_a | conjunto_b

print("\nUnião:")
print(uniao)

# 2. Interseção
# Retorna apenas os elementos que existem nos dois conjuntos.
intersecao = conjunto_a & conjunto_b

print("\nInterseção:")
print(intersecao)

# 3. Diferença
# Retorna os elementos que existem em A,
# mas não existem em B.
diferenca_a = conjunto_a - conjunto_b

print("\nDiferença (A - B):")
print(diferenca_a)

# Diferença de B em relação a A
diferenca_b = conjunto_b - conjunto_a

print("\nDiferença (B - A):")
print(diferenca_b)

# 4. Diferença simétrica
# Retorna os elementos que pertencem a apenas um dos conjuntos.
diferenca_simetrica = conjunto_a ^ conjunto_b

print("\nDiferença simétrica:")
print(diferenca_simetrica)

# 5. Adicionando elementos
conjunto_a.add(10)

print("\nConjunto A após adicionar 10:")
print(conjunto_a)

# 6. Removendo elementos
conjunto_a.remove(10)

print("\nConjunto A após remover 10:")
print(conjunto_a)

# 7. Verificando se um elemento pertence ao conjunto
print("\nO número 3 pertence ao conjunto A?")
print(3 in conjunto_a)

# 8. Verificando se um conjunto é subconjunto de outro
conjunto_c = {1, 2}

print("\nO conjunto C é subconjunto de A?")
print(conjunto_c.issubset(conjunto_a))

# 9. Verificando a quantidade de elementos
print("\nQuantidade de elementos em A:")
print(len(conjunto_a))
