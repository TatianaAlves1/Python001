try:
    with open('aula09/arquivo-teste.txt','a',encoding='utf-8') as arquivo:
        print("abriu...")
        print(arquivo.read())
except:
    print("não rolou")