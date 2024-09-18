def procura_lance_maior(dire_lances):
    winner = ""
    lance_maior = 0 
    for bidder in dire_lances:
        bid_amount = dire_lances[bidder]
        if bid_amount > lance_maior:
            lance_maior = bid_amount
            winner = bidder

    print(f"O vencedor é {winner} com o lance de R${lance_maior}.")

lances = {}
continua_lance = True
while continua_lance:
    name = input("Qual seu nome?: ")
    price = float(input("Qual seu lance?: "))
    lances[name] = price
    continua = input("Tem novos lances? Digite 'sim' para continuar ou 'nao' para parar \n").lower()
    if continua == "nao":
        continua_lance = False
        procura_lance_maior(lances)
    elif continua == "sim":
        print("\n" * 20)



