'''
Faça um programa que peça uma nota, entre zero e dez. 
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
'''
valor = ""
valor_float = 0

while True:
    valor = input('Digite um valor entre 0 e 10: ')

    try:
        valor_float = float(valor)
        if valor_float >= 1 and valor_float <= 10:
            print(f'Você digitou {valor_float}')
            break
        else:
            print('Digite números entre 0 e 10')
    except:
        print(f'{valor} não é válido')

'''
nota = float(input("Insira uma nota 0 até 10: "))

while (nota < 0) or (nota > 10):
    nota = float(input("Não pode ser menor que 0 ou maior que 10 meu jovem!\n \
    Tente novamente:"))
print("Nota válida")

'''

