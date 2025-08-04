def classificar_aluno(notas: list[float]) -> str:
    if not notas or any(n < 0 or n > 10 for n in notas):
        raise ValueError("Notas invalidas")
    media = sum(notas) / len(notas)
    if media >= 7:
        return "Aprovado"
    elif media >= 4:
        return "Recuperacao"
    else:
        return "Reprovado"