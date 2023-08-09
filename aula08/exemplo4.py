#funções empacotadas(args)
def soma(*args):
    x = sum(args)
    return x
def mostrar_maximo(*args):
    maximo = max(args)
    return maximo
def calcular_media(*coxinha):
    return sum(coxinha)/len(coxinha)
def max_min(*args):
    return max(args),min(args)
#chamadas
print(soma(2,5,12))
print(mostrar_maximo(10,-2,5-9,33))
print(mostrar_maximo(10,-2))
print(calcular_media(10,8,2,10))
print(max_min(5,6,1,2,10,-3))
tupla = max_min(5,6,1,2,10,-3)
print(f"Máximo: {tupla[0]} e o mínimo: {tupla[1]}")