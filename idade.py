while 1==1:
    idade = int(input("Digite a idade:(0 para sair) "))
    if idade == 0:
        break
    if idade >=18:
        print("Maior de idade.")
    else:
        print("Menor de idade.")