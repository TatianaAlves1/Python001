qtd = int(input("Informe:"))
notas = []
soma = 0

for i in range(1,qtd+1):
    n = int(input("nota:"))
    notas.append(n)
    soma += n  

print(notas)

# t = "texto"
# print(t.lower())