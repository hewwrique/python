alturatronco = float (input("Digite a altura do tronco da pirâmide: "))
bmenor = float (input("Digite o valor da base menor: "))
bmaior = float (input("Digite o valor da base maior: "))

volume = alturatronco / 3 * (bmaior**2 + bmenor**2 + (bmaior**2 * bmenor**2) ** 0.5 )

print(f"O valor do volume do tronco da uma pirâmide é: {volume}")

