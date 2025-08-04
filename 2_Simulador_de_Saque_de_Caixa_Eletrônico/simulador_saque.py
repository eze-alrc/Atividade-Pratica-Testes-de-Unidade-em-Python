def sacar(valor: int) -> dict:
    if valor == 0:
        raise ValueError("Valor invalido para saque")
    if valor % 10 != 0:
        raise ValueError("Somente valores multiplos de 10 sao permitidos")

    notas = [100, 50, 20, 10]
    resultado = {}
    for nota in notas:
        qtd, valor = divmod(valor, nota)
        if qtd:
            resultado[nota] = qtd
    return resultado