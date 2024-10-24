def tabela_calculo(valor_compra):
    if valor_compra < 10:
        print("lucro de 70%")
    
    elif 10 <= valor_compra < 30:
        print("lucro de 50%")
    
    elif 30 <= valor_compra < 50:
        print("lucro de 40%")

    elif valor_compra >= 50:
        print("lucro de 30%")
    else :
        print("nao se encaixa nos paramentros ")



nome_produto = str(input("digite o nome do produto :"))
valor_compra = float(input("digite o valor da compra:"))

valor_venda = tabela_calculo(valor_compra)

print(f"{nome_produto} custa {valor_compra}")
