#contagem normal
for i in range(0,10):
    print(i,end=" ")
print("\n*****")
#contagem com incremento em 2
for x in range(0,50,2):
    print(x,end=" ")
#contagem decrescente()
print("\n*****")
for j in range(100,50,-5):
    print(j,end=" ")
print("\n*****")
for x in range(1,50):
    print("*"*x)
print("\n*****")
#mostrar a tabuada do 8 com for
for y in range(1,11):
    print("8 x ",y,"=",y*8)
#leia 10 números e some somente os pares
ac = 0 
for z in range(1,1):
    n = int(input("Informe um valor inteiro:"))
    if n%2==0:
        ac +=n
print(f"Total de pares acumulados foram: {ac}") 
print("\n*****")
soma = 0
for cont in range(0,15):
     n = int(input("Informe um valor inteiro:"))
     if n < 0:
        print("Vamos encerrar") 
        break;
     soma += n 
print(f"A soma dos positivos é:{soma}")
vlr = True
while vlr:
   n =  int(input("Digita o valor: "))
   if(n<0):
    vlr=False

cont = 0
for x2 in range(1,20):
    n1 = int(input("Informe os positivos:"))
    if n1 < 0:
        continue
    print(x2)
    cont+=1    

