from chatgpt import ChatGPT
from user import UserManager
import math
import location


class Controller:

    def __init__(self):
        pass

    def distance(self, latitud_1, longitud_1, latitud_2, longitud_2): 
        latitud_1 = math.radians(latitud_1)
        longitud_1 = math.radians(longitud_1)
        latitud_2 = math.radians(latitud_2)
        longitud_2 = math.radians(longitud_2)

        distancia = 6371.01 * math.acos(
        math.cos(latitud_1) * math.cos(latitud_2) * math.cos(longitud_2 - longitud_1) +
        math.sin(latitud_1) * math.sin(latitud_2))

        return distancia


    def nearest_center(self):
        latituduser = location.latitude
        longituduser = location.longitude

        
        latitudesubis = [0.0, 100.0]
        longitudesubis = [0.0, 100.0]

        dmin = float("inf")

        for i in range(latitudesubis):
            d = self.distance(latitudesubis[i], longitudesubis[i], latituduser, longituduser)

            if d < dmin:
                dmin = d
                nearest_hospital = (latitudesubis[i], longitudesubis[i]) 

        return nearest_hospital
        

    def handle_request(self, content, id=None):
        try:
            user = UserManager().load_user(id)

            if user.first_interaction:
                return "Escriu la comanda /start per començar"

            elif content and not user.blocked:
                print("\n\n")
                print(content)
                classification = ChatGPT().get_classification(user, content)
                    
                if classification["category"] == 5:
                    self.nearest_center()
                print(classification)
                answer = ChatGPT().get_answer(user, content,str(classification["category"]))
                if classification["category"] == 1:
                    answer = ChatGPT().get_desease(user, answer["desease"])
                    
                user.record.append({"role":"user", "content": content})
                user.record.append({"role":"assistant", "content": answer})
                return answer
            
            elif user.blocked:
                return "Envia un correu a suport@hospital.com per més informació"
                
        except Exception as e:
            print("Error handle_request: " + str(e))    
        

    