#leia e armazene n números positivos
idade = int(input("Informe sua idade:"))

if idade<0 or idade>130:
    raise Exception("Idade informada está incorreta")


