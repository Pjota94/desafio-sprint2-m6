with open("CNAB.txt", "r") as arquivo:
    for value in arquivo:
        tipo = value[0:1]
        data = value[1:9]
        valor = value[9:19]
        cpf = value[19:30]
        cartao = value[30:42]
        hora_transacao = value[42:48]
        dono_loja = value[48:62]
        nome_loja = value[62:81]

        print(
            f"Tipo: {tipo} | Data: {data} | Valor: {valor} | Cpf: {cpf} | Cartao: {cartao} | Hora: {hora_transacao} | Dono: {dono_loja} | Loja: {dono_loja}"
        )
