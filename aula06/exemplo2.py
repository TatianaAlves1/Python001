lista = [1,5,6,9,8,12,0,-1]

print("Valor máximo:",max(lista))
print("Valor Mínimo:",min(lista))

lista2 =[]

for i in range(5):
    print(i+1,"-Informe um valor:", end=" ")
    num = float(input())
    lista2.append(num)

print("Valor máximo:",max(lista2))
print("Valor Mínimo:",min(lista2))
print("Quantidade de itens:",len(lista2))
print("Lista ordenada:",sorted(lista2))
print("Lista em ordem de inserção:",lista2)