dados = ('dormir','trabalhar','treinar','estudar')
dados2 = ['dormir','trabalhar','treinar','estudar']
print(type(dados))
print(type(dados2))

dados2[0] = "dormir mais"
print(dados2)
# dados[0] = 'teste'
# print(dados)
#Mostrar quantidade de ocorrências
print(dados.count("dormir"))
#mostrar o índice de um determindado item
print(dados.index("treinar"))
