dados = {}

print(type(dados))

contato = {
    'Maria':'9999-4545',
    'Ana':'3366-9852',
    'Gabriel':'1234-7894',
    'Hélio': '2345-7894' 
}
#Mostrar items do dicionário
print(contato.items())
print(contato)
print("*"*50)
#mostrar valores específicos conforme chave
print("Ana:",contato['Ana'])
print("*"*50)
#mostrar chaves do dicionário
print(contato.keys())
print("*"*50)
#Mostrar valores dos dicionários
print(contato.values())
print("*"*50)
contato['josé'] = "6987-4125"
print(contato)
print("*"*50)
#remover item específico
#contato.pop('Maria')
print(contato)
print("*"*50)
#contato.popitem()
print(contato)

print("\n for1","*"*50)
for x in contato:
    print(x, end=" ")
print("\n for2","*"*50)

for i in contato.values():
    print(i)
print("\n for 3","*"*50)

for i in contato.items():
    print(i)

print(sorted(contato.keys()))
print(sorted(contato.values()))
print(sorted(contato.items()))
