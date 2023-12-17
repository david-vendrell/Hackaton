from chatgpt import ChatGPT
from user import UserManager
import math
import location
import json
import re

from sender import Sender

class Controller:

    def __init__(self):
        pass

    def split_phrase(self, message):
        try:
            subfrases = re.split('(\.|\?)', message)
            # Combinamos cada fragmento con su delimitador correspondiente
            resultado = [subfrases[i] + (subfrases[i + 1] if i + 1 < len(subfrases) else '') for i in range(0, len(subfrases) - 1, 2)]
            # Filtramos elementos vacíos en caso de que existan
            resultado = [s for s in resultado if s]
            resultado = [frase.replace("¡", ".").replace("¿", ".").replace(".", "") for frase in resultado]
            resultado = [frase.replace("_", ".") for frase in resultado]
            return resultado
        except Exception as e:
            print("Error split_phrases: " + str(e))
            
    def distance(self, latitud_1, longitud_1, latitud_2, longitud_2): 
        latitud_1 = math.radians(latitud_1)
        longitud_1 = math.radians(longitud_1)
        latitud_2 = math.radians(latitud_2)
        longitud_2 = math.radians(longitud_2)

        distancia = 6371.01 * math.acos(
        math.cos(latitud_1) * math.cos(latitud_2) * math.cos(longitud_2 - longitud_1) +
        math.sin(latitud_1) * math.sin(latitud_2))

        return distancia


    def nearest_center(self, user):
        latituduser = user.location["la"]
        longituduser = user.location["lo"]
        
        latitudesubis = [0.0, 100.0]
        longitudesubis = [0.0, 100.0]

        dmin = float("inf")

        for i in range(latitudesubis):
            d = self.distance(latitudesubis[i], longitudesubis[i], latituduser, longituduser)

            if d < dmin:
                dmin = d
                nearest_hospital = (latitudesubis[i], longitudesubis[i]) 

        return nearest_hospital
        

    async def handle_request(self, content, id=None):
        try:
            user = UserManager().load_user(id)

            if user.first_interaction:
                return ["Escriu la comanda /start per començar"]

            if content and not user.blocked:
                print("\n\n")
                print(content)
                classification = ChatGPT().get_classification(user, content)
                    
                if classification["category"] == 5:
                    return "Ens hem adonat que la teva pregunta és una qüestió mèdica; et recomanem que consultis un especialista en aquest tema.\n\nSi ho desitges, podem posar-te en contacte amb un professional"

                print(classification)
                answer = ChatGPT().get_answer(user, content,str(classification["category"]))
                if classification["category"] == 1:
                    answer = ChatGPT().get_disease(json.loads(answer)["disease"], content)
                elif classification["category"] == 3:
                    answer = ChatGPT().get_protection(json.loads(answer)["protection"], content)
                    
                print("ANSWER: " + answer + "\n")
                user.record.append({"role":"user", "content": content})
                user.record.append({"role":"assistant", "content": answer})
                return self.split_phrase(answer)
            
            elif user.blocked:
                return "Envia un correu a suport@hospital.com per més informació"
                
        except Exception as e:
            print("Error handle_request: " + str(e))    
        

    