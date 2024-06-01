import random
import os
import time


def main():
    ganhou = int(0)
    tentativas = int(1)
    numero_secreto=random.randint(1,100)
    qtd_tentativas = int(0)
    while tentativas != ganhou:
        chute = float(input("Insira um número: "))
        if chute == numero_secreto:
            print("Parabéns você acertou o número secreto!\n"
                f"{chute}\n"
                f"Você acertou o número secreto com {qtd_tentativas} tentativas") 
            ganhou = ganhou + 1
            while escolha != "1" and escolha != "0":
                escolha = str(input("Deseja jogar novamente? (1 - Sim | 0 - Não )\n"))
                if escolha == "1":
                    os.system('cls')
                    main()
                elif escolha == "0":
                    os.system('cls')
                    print("Saindo.")
                    time.sleep(0.7)
                    print("Saindo..")
                    time.sleep(0.7)
                    print("Saindo...")
                
        elif chute < numero_secreto:
            os.system('cls')
            print(f"O número é maior que: {chute}\n")
            qtd_tentativas = qtd_tentativas + 1
        else:
            os.system('cls')
            print(f"O número é menor que: {chute}\n")   
            qtd_tentativas = qtd_tentativas + 1
        escolha = "8"
  








if __name__ == "__main__":
    main()
