import requests 
import json 
from time import sleep

def COVID(Estado): 

   try:
        covid = requests.get(f"https://covid19-brazil-api.now.sh/api/report/v1/brazil/uf/{Estado}") 
        json_data = covid.json() 

        uf = json_data["uf"] 
        state = json_data["state"] 
        cases = json_data["cases"] 
        deaths = json_data["deaths"] 
        suspects = json_data["suspects"]
        refuses = json_data["refuses"] 
        print(f'Buscando as informações no Estado {Estado.upper()}...')
        sleep(2.5)
        print('-'*35)
        print (f'    Informações do Estado {Estado}')
        print('-'*35)
        uf_msg = f"Sigla: {uf}"
        state_msg = f"\nEstado {state}"
        cases_msg = f"\nCasos: {cases}" 
        deaths_msg = f"\nMortes: {deaths}"  
        suspects_msg = f"\nSuspeitos: {suspects}" 
        refuses_msg = f'''\nRecusa: {refuses}
------------------------- '''
        all = uf_msg + state_msg + cases_msg + deaths_msg + suspects_msg + refuses_msg 
        print (all)   
   except KeyError: 
        print ("Estado Inválido")


