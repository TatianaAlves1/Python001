#soma com o retorno do cálculo
def soma2(n1,n2):
    total = n1+ n2
    return total
'''
#Chamada da função
print (soma2(5,10))

v1 = soma2(50,8)
print(v1)
print(v1/2)
'''
# Criar uma função para receber duas notas e cálcular e média
def media(v1,v2):
    m = (v1+v2)/2
    return m
#Criar uma função para receber a base e o expoente e cálcular a potência
def potencia(base,exp):
    valor = base**exp
    return valor
#Criar uma função para receber dois números e mostrar o maior
def maior(n1,n2):
    if n1>n2:
        return n1
    else:
        return n2
