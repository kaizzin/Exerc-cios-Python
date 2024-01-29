# Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. 
# Não utilize a função de potência da linguagem.

num1 = 0
num2 = 0
num1_float = 0
num2_float = 0
expo = 0
  

while True:
    try:
        num1 = input('Digite o número base: ')
        if ',' in num1:
            print('Não digite vírgula, utilize o ponto para números decimais')
            continue
        num1_float = float(num1)
    except:
        print('Digite apenas números')
        continue

    try:
        num2 = input('Digite o número expoente: ')
        if ',' in num2:
            print('Não digite vírgula, utilize o ponto para números decimais')
            continue
        num2_float = float(num2)
    except:
        print('Digite apenas números')
        continue
    
    expo = num1_float ** num2_float
    print(f'O resultado é {expo:,.2f}')
    break


# Exercício resolvido usando laço WHILE

# print("base ^ expoente:")
# base=int(input("Base: "))
# expoente=int(input("Expoente: "))

# potencia=1
# count=1

# while count <= expoente:
#     potencia *= base
#     count +=1

# print(base,"^",expoente,"=",potencia)

# Exercício resolvido usando laço FOR

# print("base ^ expoente:")
# base=int(input("Base: "))
# expoente=int(input("Expoente: "))

# potencia=1

# for count in range(expoente):
#     potencia *= base
#     count += 1

# print(base,"^",expoente,"=",potencia)