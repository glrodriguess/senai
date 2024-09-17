print("Sistema de Conversão de juros")
print("Desenvolvido por: Guilherme de Lima Francischini Rodrigues")
print("Copywrite 2024")
print("Versão 1.0")

while True:
    valorDaConta = float(input("Digite o valor da sua conta: R$ "))
    diasAtraso = int(input("Digite quantos dias foram de atraso:"))
    jurosPorDia = float(input("Digite o quanto de juros é por dia: % "))

    valorCorrigido = valorDaConta + (valorDaConta * diasAtraso * (jurosPorDia/100))

    print(f"O valor do cálculo do seus juros é: {valorCorrigido:.2f}")
    sair = input("Deseja fazer outro cálculo? <S/N>")
    if sair.upper() == "N":
        break

    print("Obrigado pela visita. Volte sempre!")