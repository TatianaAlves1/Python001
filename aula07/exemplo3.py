#operações sobre listas

lista = [2,6,9,8,20,36,1,20,7,0,2]
#criar uma lista com dobro de cada item
dobro = [i*2 for i in lista]
print(dobro)
#lista com a metade dos valores dos itens
metade  = [i/2 for i in lista]
print(metade)
#mostrar valores da lista que estão acima de 5
lista2 = [i for i in lista if i>5]
print(lista2)
nomes = ['Marcelo','Vivane','Fernanda','Ari']
#criar uma nova lista com os nomes em letras Maiúsculas
m_nomes = [i.upper() for i in nomes]
print(m_nomes)
