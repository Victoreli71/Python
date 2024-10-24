def operacao_total(operacao_sinal, valor, valor2):
    if operacao_sinal == "+" :
       resultado =  valor + valor2
    elif operacao_sinal == "-" :
        resultado = valor - valor2
    elif operacao_sinal == "*" :
        resultado = (valor * valor2)
    elif operacao_sinal == "/" :
        resultado = (valor / valor2)
    else :
        print ("não se encaixa nos parametros")
      
    return resultado

valor = float(input("digite o valor 1 :"))
valor2 = float(input("digite o valor 2 :"))
operacao_sinal =str(input("digite qual conta que voce quer realizar : "))

resul = operacao_total(operacao_sinal, valor, valor2)
print(f'resultado é {resul}')
