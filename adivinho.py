import random
print("Bem vindo ao jogo de adivinhaçao!")
print("Tente adivinhar o numero que estou pensando entre 1 e 20")
numero = random.randint(1,20)
while True:
    palpite = int(input("Qual o seu palpite?: "))
    if palpite < numero:
        print("voce chutou um numero baixo, tente novamente!")
    elif palpite > numero:
        print("voce chutou um numero alto, tente novamente!")
    elif palpite == numero:
        print(" Parabens! voce acertou")
        break