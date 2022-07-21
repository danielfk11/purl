####################
#      PURL        #
#    FRONT-END     #
####################
import requests
import time

perg = input("Digite a url que deseja analisar o codigo fonte\n-> ")

try:
    r = requests.get(f'https://www.{perg}')                                 #alteravel caso o site seja HTTP
    rtext = r.text
except:
    print("Error encotrado")

try:
    with open("save.html", "w") as purl:                                #criar o arquivo de save para poder analisar o HTML 
        print("Sucesso! exibindo informacoes em instantes...")
        time.sleep(3)
        purl.write(rtext)
        print("Front-End captado com sucesso!")
    
except:
    print("Error encontrado")

