nota1 = float(input("Primeira nota do aluno: "))
nota2 = float(input("Segunda nota do aluno: "))
media = (nota1 + nota2) / 2
print(media)
if media <= 4.9:
    print(f"Sua média foi de {media:.2f} e você foi reprovado")
elif media >= 5.0 and media <= 6.9:
    print(f"Sua média foi de {media:.2f} e você está de recuperação")
elif media >= 7.0:
    print(f"Sua média foi de {media:.2f} você foi aprovado. Parabéns")
print("Fim do programa")