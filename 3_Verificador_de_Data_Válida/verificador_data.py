def data_valida(dia: int, mes: int, ano: int) -> bool:
    import calendar

    if not (1 <= mes <= 12):
        return False
    ultimo_dia = calendar.monthrange(ano, mes)[1]
    return 1 <= dia <= ultimo_dia