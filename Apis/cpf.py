import requests 
import json 
from time import sleep

def CPF(Cpf): 
     try:
              cp = requests.get(f"http://hwid.allcenter.online:3500/base/{Cpf}") 
              json_data = cp.json() 

              cpf = json_data["dadosCPF"]["cpf"] 
              name = json_data["dadosCPF"]["nome"] 
              sexo = json_data["dadosCPF"]["sexo"] 
              nasc = json_data["dadosCPF"]["dataNascimento"]  
              print('Buscando no Banco de dados....') 
              sleep(1.0)
              print('-'*25)
              print ('   Informações do CPF')
              print('-'*25)
              cpf_msg = f"Cpf: {cpf}" 
              name_msg = f"\nNome: {name}"
              sexo_msg = f"\nSexo: {sexo}" 
              nasc_msg = f'''\nNascimento: {nasc}
----------------------------------'''
              all = cpf_msg + name_msg + sexo_msg + nasc_msg 
              print (all) 
     except KeyError:

         print ('CPF Inválido')
