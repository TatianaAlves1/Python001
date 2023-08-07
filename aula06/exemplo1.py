#estrutura de dados sequencial/ordenada de valores
lista = [5,6,'caneta',6.11,3,'oi',33]
print("Lista completa:",lista)
print(type(lista))
print("1º item da lista:",lista[0])
print("1º e 2º itens da lista",lista[0:3])
print("1º e 2º itens da lista",lista[:3])
print("último item da lista",lista[-1])
print("Mostrando do 3º item ao último:",lista[2:])
print("Quantidade de itens:",len(lista))
#funções/métodos listas
lista.append("Mais um")
print(lista)
lista.insert(2,"verdao")
print(lista)
print("="*50)
#teste de listas
lista_b = lista.copy()
lista2 = lista

lista_b.append("teste b")
lista2.append("Teste lista 2")
lista2.append(587)
print("Lista 1:",lista)
print("Lista 2:",lista2)
print("Lista b:", lista_b)
lista_c = [100,200,300,450,500]
lista.extend(lista_c)
print("Lista 1:",lista)
print(lista_b.count(33))
print("Lista Antes:",lista)
lista.pop()

lista.remove(3)
print("Lista Depois:",lista)
print(3 in lista)
print("Lista Depois:",lista)
# lista.clear()
print("Lista Depois:",lista)

l1 = [2,5,6]
l2 = [10,20,30]
print(l1+l2)

def soma(a,b):
    return a+b

lista5 = map(soma,l1,l2)
print(list(lista5))