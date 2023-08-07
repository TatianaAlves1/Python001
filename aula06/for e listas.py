pc = ['mouse','teclado','memória','SSD']
for i in pc:
   print(i)

unidade = ['cm','m','mm']
a = input("unidade:")
if a in unidade:
   print("presente na lista")


pc2 = ['mouse','teclado',['memória Ram','ROM','Flash'],'SSD']
cont = 0
j=0

while cont < len(pc2):  
    if cont==2:
       while j < len(pc2[2]):
           print(pc2[cont][j])
           j+=1
       continue
    print(pc2[cont])
    cont+=1

#Inserir dados ao final da lista
pc2.append("Cooler")
print(pc2)
#inserir dado identificando posição e valor
pc2.insert(1,"Teste")
print(pc2)
#pc2.sort()
print(pc2)
pc2.remove("Teste")
print(pc2)
pc2.pop(1)
print(pc2)
print(pc2[0:1])