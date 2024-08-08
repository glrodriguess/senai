limite = int(input("DIgite um numero: "))
print("contando...")
x = 2
for contador in range(limite):
    print(" a soma de",contador,"+",x,"=",contador+x)
    x = x + 1