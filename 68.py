def exercicio_68():
    def calculadora(num1, num2, operacao):
        if operacao == 'soma':
            return num1 + num2
        elif operacao == 'subtracao':
            return num1 - num2
        elif operacao == 'multiplicacao':
            return num1 * num2
        elif operacao == 'divisao':
            if num2 == 0:
                return "Erro: Divisão por zero não é permitida."
            return num1 / num2
        else:
            return "Erro: Operação inválida. Escolha 'soma', 'subtracao', 'multiplicacao' ou 'divisao'."

    while True:
        try:
            valor1 = float(input("Digite o primeiro número: "))
            valor2 = float(input("Digite o segundo número: "))
            op = input("Digite a operação ('soma', 'subtracao', 'multiplicacao', 'divisao'): ").lower()
            
            resultado = calculadora(valor1, valor2, op)
            print(f"Resultado: {resultado}")
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite números para os operandos.")
