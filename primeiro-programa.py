cont = int(input("Digite quantas notas o aluno tem: "))
nota = 0
soma = 0

for i in range(0, cont):
    nota = float(input(f"Digite a primeiro nota {i + 1}: "))
    soma += nota

media = soma / cont
print(media)
