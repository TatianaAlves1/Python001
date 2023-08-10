#defina um inteiro aleatório de 1 até 100
#faça a leitura de inteiros até o usuário adivinhar
import random

n1 = random.randint(1,100)
print(n1)
while True:
    try:
        n2 = int(input("informe o valor:"))
        if n1==n2:
            print("Parabéns!!!")
            break
    except:
        print("Valor informado incorreto")
            
        
