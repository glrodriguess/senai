print("Sistema de Conversão do Dólar")
print("Desenvolvido por: Guilherme de Lima Francischini Rodrigues")
print("Copywrite 2024")
print("Versão 1.0")

while True:
    valorEmDolar = float(input("Valor do produto em dólar: US$"))
    cotacaoDolarHoje = float(input("Digite a cotação do dólar: R$"))
    
    valorConvertido = valorEmDolar * cotacaoDolarHoje
    
    print(f"O valor convertido de US$ {valorEmDolar} é: R$ {valorConvertido}")
    sair = input ("Deseja converter outro valor? <S/N>")
    if sair.upper() == "N":
        break

    print("Obrigado pela visita. Volte sempre!")