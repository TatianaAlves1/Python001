soma = 0
cont = 1
#leia 10 números positivos e some os valores informados
while cont<=4:
    num = int(input("Informe um número positivo:"))
    if num<0:
        print("Tá maluco?")
        continue
    soma += num
    cont += 1
print(f"O total dos valores informados é {soma}")
print(f"A quantidade de valores informados foi {cont-1}")

soma = 0
cont  = 1

while cont<=5:
    num = int(input("Informe um valor negativo:"))
    if num > 0:
        print("Fim do programa!!!")
        break
    soma += num
    cont +=1

print(f"O total dos valores informados é {soma}")
print(f"A quantidade de valores informados foi {cont-1}")