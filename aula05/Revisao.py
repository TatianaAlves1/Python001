for i in range(9):
    print(i,end=" ")
print("\nValor do i:",i)
for i in range(10,21):
    print(i,end=" ")
print("\nValor do i:",i)
for i in range(10,100,5):
    print(i,end=" ")
print("\nValor do i:",i)
for i in range(50,10,-1):
    print(i,end=" ")
print("\nValor do i:",i)
v1 = 9
v2 = 50
for i in range(v1,v2):
    print(i,end=" ")
print("\nValor do i:",i)

#leia 10 números e mostre msg informando que o número é ímpar e efetue a soma dos valores
soma=0 
for i in range(0,11):
    num = float(input("Informe o número:"))
    if num%2!=0:
        print("Você digitou um número ímpar!")
        soma +=num
print("A soma dos números ímpares é ",soma)

#leia 10 números inteiros e informe ao final quantos números pares foram digitados e soma total dos valores
cont = 0
soma = 0
for i in range(1,11):
    num = int(input("Informe um número inteiro:"))
    if num%2==0:
        cont +=1
        soma +=num
print(f"A quantidade de números pares digitados foi {cont} e o soma total ficou em {soma}")
    