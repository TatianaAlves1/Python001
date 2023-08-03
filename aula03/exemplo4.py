#Estrutura de repetição While
cont = 0
while cont<=100:
    print(cont,end=" ")
    cont = cont+1
print("\nValor final do contador:",cont)
print("-"*50)
#Contagem iniciando em 50 até 200
cont = 50
while cont<=200:
    print(cont,end=" ")
    cont += 1
print("-"*50)
#Contagem iniciando em 10 e finalizando em 80, incrementando os valores de 10 em 10
cont = 10
while cont<=80:
    print(cont,end=" ")
    cont += 10
print("\n","-"*50)
#Mostrar a mensagem "Eu tenho que estudar!" 300x
cont = 1
while cont<=300:
    print(cont,"- Eu tenho que estudar!!!")
    cont += 1
# leia um número e mostre a contagem a partir de zero até o número informado
vlr_final = int(input("Informe o valor final:"))
cont = 0
while cont<=vlr_final:
    print(cont,end=" ")
    cont +=1 
print("\n","-"*50)
#Contagem decrescente iniciando em 23 até 0
cont = 23
while cont>=0:
    print(cont,end=" ")
    cont-=1
#leia 2 números e mostre a contagem do intervalo dos valores informados
n1 = int(input("Informe o valor inicial da contagem:"))
n2 = int(input("Informe o valor final da contagem:"))

while n1<=n2:
    print(n1)
    n1 += 1

