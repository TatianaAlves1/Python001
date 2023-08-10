#executar uma divisão
try:
    numerador   = float(input("Informe o numerador:"))
    denominador = float(input("Informe o denominador:"))
    print(f"O resultado da divisão é:{numerador/denominador:.2f}")
except ZeroDivisionError:
    print("Esta operação não pode ser realizada com denominador zero")
except ValueError:
    print("Verifique os valores informados\nSerão aceitos somente números....")
else:
    print("Parabéns!!! Nenhum erro foi detectado.")