while True:
    try:
        nome = input("Digite o nome:")
        idade = int(input("Digite a idade:"))
        with open('aula09/aula09.txt','a+',encoding='utf-8') as txt:
            txt.write(f"Aluno: {nome:^15} idade: {idade:^6}\n")
            try:
                n = int(input("1 -  para visualizar\nQualquer tecla para encerrar:"))
                if n == 1:
                    txt.seek(0)
                    print(txt.read())
            except:
                break
    except:
        print("Deu erro =(")