def calculo_expressao_volume(h,Bmaior,Bmenor):
    volume = (h/3) * (Bmaior*2 + Bmenor + (Bmaior * Bmenor)*0.5)
    return volume 


h = float(input("digite o valor da altura do tronco da piramide :"))
Bmenor = float(input("digite o valor da BASE MENOR :"))
Bmaior = float(input("digite o valor da BASE MAIOR :"))

volume = calculo_expressao_volume(h,Bmaior,Bmenor)

print(f"o volume do tronco da piramide é:{volume:.2f}")
