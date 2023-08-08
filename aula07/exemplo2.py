alunos = {
    111:'Saulo Souza',
    222:'Marcelo Freitas',
    333:'Ricardo Melo',
    444:'Fernanda Farias',
    555:'Alice Sena'
}
lista = [3,9,8,5,2]
lista2 = ['a','b','c','d','e']
print(type(alunos))
print(alunos[222])
alunos.update({666:"Julia Santos"})
print(alunos)
print(alunos.get(333))
teste = alunos.fromkeys(lista,lista2)
print(teste)
alunos.pop(111)
print(alunos)
print(alunos.values())
print(alunos.keys())
print(alunos.items())
for x in alunos.keys():
    print(x)
for i in alunos.values():
    print(i)
for b,c in alunos.items():
    print(b,c,sep=" - ")