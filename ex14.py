# Entrada

produto = input("Nome do produto: ")
quantidade = int(input("Quantidade: "))
preco_unitario = float(input("Preço unitário: R$ "))

# Cálculo

total = quantidade * preco_unitario

# Saída

print() # linha em branco para separar
print(f"Produto: {produto}")
print(f"Quantidade: {quantidade}")
print(f"Preço unitário: R$ {preco_unitario:.2f}")
print(f"Valor total: R$ {total:.2f}")