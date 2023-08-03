valor1 = 45
valor2 = 258.45

#operadores aritméticos
print("Soma:",valor1+valor2)
print("Subtração:",valor1-valor2)
print("Multiplicação:",valor1*valor2)
print("Divisão:",valor1/valor2)
print(f"Divisão com 2 casas decimais: {valor1/valor2:.2f}")
print(f"valor 2: {valor2:.1f}")
#Obter dados do teclado (Entrada de dados)
usuario = input("Informe o seu nome:")
print(f"Seja bem-vindo(a), {usuario}")
#Conversão de tipo de dados - Casting
idade = int(input("Informe sua idade:"))
print(f"O nome do usuário é {usuario} e sua idade atual é {idade}")
#Mostrar o dobro da idade informada pelo usuário
print(f"O dobro da idade é: {idade*2}")
#mostrar tipos dados das variáveis
print("Idade:",type(idade))
print("Usuario:",type(usuario))
valor_curso = float(input("Informe o valor pago pelo curso:"))
print(f"O valor informado foi {valor_curso}")
#mostrar uma msg com 25% do valor curso
#Parabéns!!! vc ganhou <valor> de crédito na próxima compra
vlr_desconto = valor_curso * 0.25
print(f"Parabéns!!! vc ganhou {vlr_desconto} de crédito na próxima compra")
#Solicitar quantidade de parcelas do pagamento
parcelas = int(input("Informe a qtd de parcelas para pagamento:"))
#mostrar valor das parcelas sem juros
print(f"O valor de cada parcela será de R$ {valor_curso/parcelas:.2f}")