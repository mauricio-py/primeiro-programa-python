opcao = False
quantNotas = 0
notas = []  

def leitorNotas():
    global quantNotas, notas 
    quantNotas = int(input("\nQuantas notas você deseja calcular? \n"))
    notas = [0] * quantNotas  

    for i in range(quantNotas):
        notas[i] = float(input(f"Digite a {i + 1}ª nota: "))  

def media():  
    leitorNotas()  
    soma = sum(notas)  
    media = soma / quantNotas  
    print(f"\nA média é {media:.2f} \n")  

def somaSalva(): 
    if notas:  
        soma = sum(notas)  
        print(f"\nA soma das notas é {soma:.2f} \n")  
    else:
        print("\nNenhuma nota foi inserida ainda. Primeiro, calcule a média para inserir as notas.")

def somaNaoSalva():
    notas_temp = []  
    quantNotasTemp = int(input("\nQuantas notas você deseja somar? \n"))

    for i in range(quantNotasTemp):
        nota = float(input(f"Digite a {i + 1}ª nota: "))
        notas_temp.append(nota)  

    soma = sum(notas_temp)  
    print(f"\nA soma das notas é {soma:.2f} \n")  

while True:
    opcao = int(input("""\nEscolha uma opção:
[ 1 ] Fazer a média do aluno
[ 2 ] Somar notas já utilizadas na média
[ 3 ] Somar notas sem salvar
[ 0 ] Sair do programa \n
"""))

    match opcao:
        case 1:
            media()

        case 2:
            somaSalva()

        case 3:
            somaNaoSalva()

        case 0:
            print("Saindo do programa...")
            break

        case _:
            print("Opção inválida. Tente novamente.")
