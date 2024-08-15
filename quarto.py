# idade = int(input("Digite a sua idade: "))
# for contador in range(idade+1):
#     print(contador)

sair = "N"
while sair != "S":
    nome = input("Digite um nome: ")
    for letra in nome:
        print(letra)
    print("**************")
    sair = input("Sair do programa (S/N):" )