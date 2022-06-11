
import json
from time import sleep 
import requests 

#KeyError
def CEP(cep): 
    
  try:
            cep = requests.get(f"https://cep.awesomeapi.com.br/json/{cep}")
            json_data = cep.json() 

            cepp = json_data["cep"]
            address_name = json_data["address_name"] 
            address = json_data["address"] 
            state = json_data["state"] 
            district = json_data["district"]
            lat = json_data["lat"]
            lng = json_data["lng"]
            city = json_data["city"]
            ddd = json_data["ddd"]   
            print('Analisando o Cep...')
            sleep(2.5)
            print('-'*25)
            print ('   Informações do CEP')
            print('-'*25)
            cepp_msg = f"CEP: {cepp}" 
            address_name_msg = f"\nNome do Endereço: {address_name}"
            address_msg = f"\nEndereço: {address}" 
            state_msg = f"\nEstado: {state}" 
            district_msg = f"\nDistrito: {district}" 
            lat_msg = f"\nLat: {lat}" 
            lng_msg = f"\nLng: {lng}"  
            city_msg = f"\nCidade: {city}" 
            ddd_msg = f'''\nDD: {ddd}
------------------------- '''
    

        
            all = cepp_msg + address_name_msg + address_msg + state_msg + district_msg + lat_msg + lng_msg + city_msg + ddd_msg
            print (all) 
    
  except KeyError:  
       
       print ('CEP Inválido, Verifique se está tudo correto. ')

