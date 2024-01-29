'''
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
mostrando uma mensagem de erro e voltando a pedir as informações.
'''
import os

usuario = ''
senha = ''

while True:
    usuario = input('Informe o nome de usuário: ')
    senha = input('Informe a senha: ')

    if senha in usuario:
        print('A Senha não pode ser igual ao Usuário')
        continue
    
    if senha != usuario:
        os.system('cls')
        print('Você fez o cadastro com sucesso')
        break

# login = input("Login: ")
# senha = input("Senha: ")

# while login == senha:
#     print("Sua senha deve ser diferente do login: ")
#     senha = input("Senha: ")

# print("Cadastro aprovado")
    