import requests  
import json
from time import sleep 
from Apis import covid,ip,cepp,cpf
from rich.console import Console
from os import system
from Logo import logo

console = Console()
def escreval(txt): 
       tam = len(txt) +6
       print('-'*tam) 
       print (f'   {txt}')
       print('-'*tam) 

def menu():

  
    console.print('__________________________________')
    console.print('|[[blue]1[/]] [white]Consulta de CPF[/]            |')
    console.print('|[[blue]2[/]] [white]Consulta de IP[/]             |') 
    console.print('|[[blue]3[/]] [white]Consulta de CEP[/]            |') 
    console.print('|[[blue]4[/]] [white]Consulta de COVID[/]          |')
    console.print('|[[blue]5[/]] [white]Criadores[/]                  |')
    console.print('|_______________________________|') 
    console.print('|[[red]0[/]] [white]Sair[/]                       |')
    console.print('|_______________________________|')
        

    opcao = int(input("==> "))  

  
    if opcao == 1: 

       Cpf = int(input('Informe o CPF (Sem pontuações ):  '))
       cpf.CPF(Cpf) 

       confirm = str(input('Deseja continuar? [S/N]')).strip().upper()
       if confirm == "S": 
           system('cls||clear')
           logo.logo()
           logo.bru()
           return menu()
           
       elif confirm == "N": 
                print ('Saindo...') 
                sleep(1.5)
                print ('Programa finalizado')
    elif opcao == 2: 
        IP = input('Informe o Ip (Com pontuação):  ')
        ip.ip(IP)

        confirm = str(input('Deseja continuar? [S/N]')).strip().upper()
        if confirm == "S": 
           system('cls||clear')
           logo.logo()
           logo.bru()
           return menu()

        elif confirm == "N": 
                print ('Saindo...') 
                sleep(1.5)
                print ('Programa finalizado')


    elif opcao == 3:  
        cep = input("Informe o CEP (Sem pontuações): ")
        cepp.CEP(cep)

        confirm = str(input('Deseja continuar? [S/N]')).strip().upper()
        if confirm == "S": 
           system('cls||clear')
           logo.logo()
           logo.bru()
           return menu()

        elif confirm == "N": 
                print ('Saindo...') 
                sleep(1.5)
                print ('Programa finalizado')


    elif opcao == 4: 
            Estado = str(input("Informe a silga do seu estado: ")).strip().upper()
            covid.COVID(Estado) 
            confirm = str(input('Deseja continuar? [S/N]')).strip().upper()

            if confirm == "S": 
               system('cls||clear')
               logo.logo()
               logo.bru()
               return menu() 

            elif confirm == "N": 
                print ('Saindo...') 
                sleep(1.5)
                print ('Programa finalizado')
    
    elif opcao == 0: 
        print ('Saindo...') 
        sleep(1.5)
        print ('Programa finalizado')

    elif opcao == 5: 
      console.print('_________-[cyan]CRIADORES[/]-____________')
      console.print('|[magenta]insta[/]: [white]@thor.dress[/]            |')
      console.print('|          [purple]Back-end[/],[purple]Desing[/]     |')
      console.print('|[magenta]insta[/]: [white]@ocean.romanov[/]         |')
      console.print('|           [purple]Apis[/],[purple]Desing[/]        |')
      console.print('|______________________________|')  
      confirm = str(input('Deseja continuar? [S/N]')).strip().upper()
      if confirm == "S": 
               system('cls||clear') 
               logo.logo()
               logo.bru()
               return menu()

      elif confirm == "N": 
                print ('Saindo...') 
                sleep(1.5)
                print ('Programa finalizado')