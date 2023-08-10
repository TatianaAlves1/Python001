#abertura de arquivos
try:
    txt = open("aula09/dados.txt",'r',encoding='UTF-8')
    print(txt.read())
except:
    print("Arquivo não existe!!!")
else:
    txt.close()

