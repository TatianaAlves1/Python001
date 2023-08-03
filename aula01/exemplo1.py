#Primeiro script em Python
print("Hello, World!!!")
print('Curso Programando com Python')
print('-'*20)
print("Carga horária: 40h \n10 dias")
#padrão snake case
nome_pessoa = "Tatiana Alves"
nome_curso  = "Programando com Python"
idade =  10
valor_curso = 250.99
#mostrar tipos de dados das variáveis 
print(type(nome_pessoa))
print(type(idade))
print(type(valor_curso))
#concatenar dados
print("Seja bem-vindo(a)",nome_pessoa)
print("Seja bem-vindo(a)",nome_pessoa,"ao curso",nome_curso)
#o curso <nome_curso> custa <valor>
print("O curso",nome_curso,"custa R$",valor_curso)
#f-strings no python
print(f"seja bem-vindo {nome_pessoa}")
print(f"O valor do curso {nome_curso} é {valor_curso}")
