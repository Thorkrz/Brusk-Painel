import requests 
import json
from time import sleep
def ip(IP): 

   try:
        i = requests.get(f"https://hadesconsulta.000webhostapp.com/api/ipsearch.php?ip={IP}") 

        json_loads = i.json()
        ip = json_loads["query"]  
        conti = json_loads["continent"] 
        country = json_loads["country"]
        countryCode = json_loads["countryCode"] 
        region = json_loads["region"] 
        regionName = json_loads["regionName"] 
        city = json_loads["city"] 
        org = json_loads["org"] 
        mobile = json_loads["mobile"]
        print ('Carregando as informações...')
        sleep(2.5)
        print('-'*25)
        print ('   Informações do IP')
        print('-'*25) 
        ip_msg = f"IP: {ip}" 
        conti_msg = f"\nContinente: {conti}" 
        country_msg = f"\nPaís: {country}" 
        countryCode_msg = f"\nCódigo do País: {countryCode}" 
        region_msg = f"\nRegião: {region}" 
        regionName_msg = f"\nNome da Região: {regionName}" 
        city_msg = f"\nCidade: {city}" 
        org_msg = f"\nOrg: {org}" 
        mobile_msg = f'''\nÉ Moblie? {mobile}
----------------------------------'''
 
        all = ip_msg + conti_msg + country_msg + countryCode_msg + region_msg +  regionName_msg + city_msg + org_msg + mobile_msg
        print (all)  
   except: 
           print ('IP Inválido')
#ip("170.245.79.18")