opcao = False

def media():
  notas = 0
  quantNotas = int(input("\nQuantas notas você deseja calcular a média? "))
  for i in range(0, quantNotas, 1):
    nota = int(input(f"Digite a nota {i + 1}ª: "))
    notas += nota
    print(notas)
  print(quantNotas)  
  media = notas / quantNotas
  print(f"\n a media é {media} \n")

while True:
  opcao = int(input("""[ 1 ] fazer a media de aluno
[ 0 ] sair do programa \n
  """))
  
  if opcao == 1:
    media()
  
  
  if opcao == 0:
    break
