import os
import time
import random
from datetime import date
#import time
data_atual = date.today()
data_atual = '{}/{}/{}' .format(data_atual.day, data_atual.month, data_atual.year)

clientes = [{"nome":"João Oliveira",
             "idade":"22",
             "peso":"50",
             "altura":"1.78",
             "imc":"15.78",
             "classificacao_Imc":"Abaixo do peso",
             "personal":"Ana Luiza"},

            {"nome":"Pedro Henrique",
             "idade":"19",
             "peso":"78",
             "altura":"1.85",
             "imc":"22.79",
             "classificacao_Imc":"Peso ideal",
             "personal":"Matheus Felipe"}]


fucionarios = ["Eric Patrick", "Ana Luiza", "Matheus Felipe"]


def entrada_invalida():
    input("O valor inserido não é válido.\n"
          "\nDigite qualquer tecla para retornar ao menu principal: ")
    main()


#MENU INICIAL
def inicio():
    os.system('cls')
    print("\n"f"- - - - - - - - ＡＣＡＤＥＭＩＡ ＦＡＵＳＴＩＮＯ - - - - - - - -   {data_atual}\n")
    print("1- Cadastrar Cliente\n"
          "2- Clientes Registrados\n"
          "3- Personal Trainers Registrados\n"
          "4- Sair\n")

#CADASTRAMENTO DE CLIENTE
def cadastrar_Cliente():
    os.system('cls')
    print("- - - 𝖢𝖠𝖣𝖠𝖲𝖳𝖱𝖠𝖬𝖤𝖭𝖳𝖮 𝖣𝖤 𝖢𝖫𝖨𝖤𝖭𝖳𝖤 - - -")   
    nome_Novo_Cliente = input("\nInsira o nome do cliente: ")
    try:
        idade_Novo_Cliente = int(input("\nInsira a idade do cliente: "))
    except ValueError:
        os.system('cls')
        entrada_invalida()

    try:
        Peso_Novo_Cliente = float(input("\nInsira o Peso do cliente (em kg): "))
    except ValueError:
        os.system('cls')
        entrada_invalida()

    try:
        altura_Novo_cliente = float(input("\nInsira a altura do cliente: EX: 0.00 : "))
    except ValueError:
        os.system('cls')
        entrada_invalida()

    imc = Peso_Novo_Cliente / (altura_Novo_cliente*altura_Novo_cliente)
    
    if imc <= 18.5:
        classificacao_imc = "Abaixo do peso"
    elif imc >= 18.6 and imc <= 24.9:
        classificacao_imc = "Peso ideal"
    elif imc >= 25 and imc <= 29.9:
        classificacao_imc = "Levemente acima do peso"
    elif imc >= 30 and imc <= 34.9:
        classificacao_imc = "Obesidade grau I"
    elif imc >= 35 and 39.9:
        classificacao_imc =  "Obesidade grau II"
    else:
        classificacao_imc =  "Obesidade grau III"

    personal = random.choice(fucionarios)
    
    #ADICIONAR DADOS DO CLIENTE AO DICIONÁRIO
    dados_Cliente = {"nome": str(nome_Novo_Cliente),
                     "idade": str(idade_Novo_Cliente),
                     "peso":str(Peso_Novo_Cliente),
                     "altura":str(altura_Novo_cliente),
                     "imc": f"{imc:.5}",
                     "classificacao_Imc":str(classificacao_imc),
                     "personal":str(personal)
                     }
    
    clientes.append(dados_Cliente)

    os.system('cls\n')
    print(f"- - - 𝖢𝖠𝖣𝖠𝖲𝖳𝖱𝖮 𝖣𝖤 𝖢𝖫𝖨𝖤𝖭𝖳𝖤 - - - {data_atual}\n"
          f"Nome: {nome_Novo_Cliente}              Idade: {idade_Novo_Cliente}\n"
          f"Peso: {Peso_Novo_Cliente}              Altura: {altura_Novo_cliente}\n"
          f"IMC: {imc:.5}             Classificação do IMC: {classificacao_imc}\n"
          f"\nPersonal Trainer: {personal}") 
    
    input("\nDigite qualquer botão para voltar: ")
    os.system('cls')
    main()
    return dados_Cliente

#LISTAR CLIENTES    
def  listar_Clientes():
    os.system('cls')
    print("- - - 𝖢𝖫𝖨𝖤𝖭𝖳𝖤𝖲 𝖱𝖤𝖦𝖨𝖲𝖳𝖱𝖠𝖣𝖮𝖲 - - -\n")
    print(f"{"ID".ljust(2)}| {"NOME".ljust(15)}| {"IDADE".ljust(15)}| {"PESO".ljust(15)}| {"ALTURA".ljust(15)}| {"IMC".ljust(15)}| {"CLASSIFICAÇÃO".ljust(15)}| {"PERSONAL TRAINER".ljust(5)} ")
    i = 1
    for cliente in clientes:
        cliente_Nome = cliente["nome"]
        cliente_Idade = cliente["idade"]
        cliente_Peso = cliente["peso"]
        cliente_Altura = cliente["altura"]
        cliente_Imc = cliente["imc"]
        cliente_Classificacao_Imc = cliente["classificacao_Imc"]
        cliente_Personal = cliente["personal"]

        print(f"{str(i).ljust(2)}| {cliente_Nome.ljust(15)}| {cliente_Idade.ljust(15)}| {str(cliente_Peso).ljust(15)}| {str(cliente_Altura).ljust(15)}| {str(cliente_Imc).ljust(15)}| {cliente_Classificacao_Imc.ljust(15)}| {cliente_Personal.ljust(5)}") 
        i = i + 1

    input("\nDigite qualquer botão para voltar: ")
    os.system('cls')
    main()
    
    
#LISTAR PERSONAL TRAINER
def listar_Personal():
    os.system('cls')
    print("- - - 𝖯𝖤𝖱𝖲𝖮𝖭𝖠𝖫 𝖳𝖱𝖠𝖨𝖭𝖤𝖱𝖲 𝖱𝖤𝖦𝖨𝖲𝖳𝖱𝖠𝖣𝖮𝖲 - - -\n")
    i = 0
    for funcionario in fucionarios:
        print(fucionarios[i]) 
        i = i + 1
    input("\nDigite qualquer botão para voltar: ")
    os.system('cls')
    main()

#FINALIZAR SISTEMA
def finalizar_System():
    os.system('cls')
    print("Saindo.")
    time.sleep(0.5)
    os.system('cls')
    print("Saindo..")
    time.sleep(0.5)
    os.system('cls')
    print("Saindo...")


#ESCOLHER OPÇÃO
def escolher_opcao():
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        cadastrar_Cliente()
    elif opcao == "2":
        listar_Clientes()
    elif opcao == "3":
        listar_Personal()
    elif opcao == "4":
        finalizar_System()
    else:
        os.system('cls')
        print("Opção inválida")
        time.sleep(0.7)
        os.system('cls')
        inicio()
        print("Escolha uma opção listada acima\n")
        escolher_opcao()        
 


def main():
    inicio()
    escolher_opcao()
    

if __name__ == '__main__':
    main()