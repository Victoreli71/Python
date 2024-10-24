def realizar_operacao():
    while True:
        # Solicita ao usuário que informe dois números e uma operação
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação (+, -, *, /): ")

        # Realiza a operação com base na escolha do usuário
        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            if num2 != 0:
                resultado = num1 / num2
            else:
                print("Erro: divisão por zero não permitida.")
                continue  # Volta para o início do loop
        else:
            print("Operação inválida. Tente novamente.")
            continue  # Volta para o início do loop

        # Exibe o resultado
        print(f"O resultado é: {resultado}")

        # Pergunta se o usuário deseja realizar outra operação
        nova_operacao = input("Deseja realizar outra operação? (sim/não): ").strip().lower()
        if nova_operacao != 'sim':
            print("Encerrando o programa.")
            break  # Sai do loop, encerrando o programa

# Chama a função para iniciar o programa
realizar_operacao()
