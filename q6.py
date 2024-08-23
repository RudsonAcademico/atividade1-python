# Construa um pseudocódigo que informe se o aluno foi aprovado, reprovado ou fará uma nova avaliação (recuperação) em uma determinada disciplina

nota1 = int(input("Digite a primeira nota do aluno: "))
nota2 = int(input("Digite a segunda nota do aluno: "))
nota3 = int(input("Digite a terceira nota do aluno: "))

media = (nota1+nota2+nota3)/3

if media >= 70:
    print("Aprovado")
elif media >= 50 and media < 70:
    print("Recuperação")
else:
    print("Reprovado")