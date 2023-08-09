def dicionario(**kwargs):
    for k, v in kwargs.items():
        print(f"A chave é = {k} e o valor é {v}")
    return kwargs    

teste = dicionario(nome="Tati",cpf="4548787",email="34234@gmail.com")
print(teste.keys())

def total_impostos(nome,**kwargs):
    print(f"Funcionário {nome} receberá descontos de {sum(kwargs.values())}") 

total_impostos(nome="Tati",ir=100,fgts=500,pensao=125)
total_impostos(nome="Outro",fgts=200,transporte=40)