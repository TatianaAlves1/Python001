#Estruturas de decisão(Condicionais)
"""
Leia a idade do aluno e defina sua categoria de acordo com as seguintes informações:
Categoria - idade
Sem categoria - Menor do que 3
Infantil - 3 até 10
Juvenil - 11 até 17
adulto - 18 até 39
senior - 40 até 130
acima de 130 idade inválida
"""
idade = int(input("Informe a idade do aluno:"))

if idade<3:
    print("Aluno Sem categoria definida")
elif idade<=10:
    print("Aluno da categoria Infantil")
elif idade<=17:
    print("Aluno da categoria Juvenil")
elif idade<=39:
    print("Aluno da categoria Adulto")
elif idade<=130:
    print("Aluno da categoria Senior")
else:
    print("Idade inválida!!!")





