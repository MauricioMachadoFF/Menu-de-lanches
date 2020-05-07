#coding: utf-8;
from time import sleep 
from os import system

total = 0.00

def option1():
    global total
    print("----------------------------------------------")
    print("[1] Salgados")
    print("[2] Bebidas")
    print("[3] Sobremesas")
    print("[4] Valor Da Compra")
    print("[5] Finalizar pedido")
    print("----------------------------------------------")
    op = int(input())
    while(op < 1 and op > 5):
        op = int(input())

    if(op == 1):
        system("clear")
        print("Carregando...")
        sleep(2)
        option2()


    elif(op == 2):
        system("clear")
        print("Carregando...")
        sleep(2)
        option3()
    
    elif(op == 3):
        system("clear")
        print("Carregando...")
        sleep(2)
        option4()
    
    elif(op == 4):
        system("clear")
        print("Carregando...")
        sleep(2)
        print(total)


    elif(op == 5):
        system("clear")
        print("Carregando...")
        sleep(2)
        print("Total da Compra: R${}".format(total))
        print("Muito Obrigado! Volte Sempre!!!!")
    
        
        

def option2():
    global total
    print("----------------------------------------------")
    print("[1] Pão de Queijo: R$ 6,00")
    print("[2] Coxinha: R$ 8,00")
    print("[3] Risoles: R$ 10,00")
    print("[4] Sanduíche: R$ 14,00")
    print("[5] Voltar")
    print("----------------------------------------------")
    ch = 1
    while(ch != 5):
        ch = int(input())
        if(ch == 1):
            total = total + 6.00
            print(total)
            print("Item adicionado com sucesso.")
        elif(ch == 2):
            total = total + 8.00
            print(total)
            print("Item adicionado com sucesso.")
        elif(ch == 3):
            total = total + 10.00
            print(total)
            print("Item adicionado com sucesso.")
        elif(ch == 4):
            total = total + 14.00
            print(total)
            print("Item adicionado com sucesso.")
        elif(ch == 5):
            system("clear")
            print("Carregando...")
            sleep(2)
            option1()        
        else:
            print("O pedido que você deseja não existe. Tente de novo em outro universo.")
    

def option3():
    global total
    print("----------------------------------------------")
    print("[1] Água: R$2,00")
    print("[2] Guaraná: R$5,00")
    print("[3] Coca-Cola: R$7,00")
    print("[4] Suco Natural: R$7,00")
    print("[5] Voltar")
    print("----------------------------------------------")
    ch = 1
    while(ch != 5):
        ch = int(input())

        if(ch == 1):
            total = total + 2.00
            print(total)
            print("Item adicionado com sucesso.")

        elif(ch == 2):
            total = total + 5.00
            print(total)
            print("Item adicionado com sucesso.")

        elif(ch == 3):
            total = total + 7.00
            print(total)
            print("Item adicionado com sucesso.")

        elif(ch == 4):
            total = total + 7.00
            print(total)
            print("Item adicionado com sucesso.")

        elif(ch == 5):
            system("clear")
            print("Carregando...")
            sleep(2)
            option1()
        
        else:
            print("O pedido que você deseja não existe. Tente de novo em outro universo.")

def option4():
    global total
    print("----------------------------------------------")
    print("[1] Cookie: R$ 6,00 (1 unidade)")
    print("[2] Brigadeiro de Pote: R$ 10,00")
    print("[3] Bolo de Chocolate: R$ 12,00 (1 fatia)")
    print("[4] Torta de Banoffe: R$ 14,00")
    print("[5] Voltar")
    print("----------------------------------------------")
    ch = 1
    while(ch != 5):
        ch = int(input())
        
        if(ch == 1):
            total = total + 6.00
            print(total)
            print("Item adicionado com sucesso.")

        elif(ch == 2):
            total = total + 10.00
            print(total)
            print("Item adicionado com sucesso.")

        elif(ch == 3):
            total = total + 12.00
            print(total)
            print("Item adicionado com sucesso.")

        elif(ch == 4):
            total = total + 14.00
            print(total)
            print("Item adicionado com sucesso.")

        elif(ch == 5):
            system("clear")
            print("Carregando...")
            sleep(2)
            option1()
        
        else:
            print("O pedido que você deseja não existe. Tente de novo em outro universo.")

option1()

