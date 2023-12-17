import openai
import json

from prompts import Prompts

openai.organization = "org-7Xlzvwkj0VnvG7N6xeNY1RN4"
openai.api_key = "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"

class ChatGPT: 

    def get_response(self, messages):
        try:
            print("Holaaaa")   
            
            print("Message: " + str(messages))
            response = openai.chat.completions.create(
                model="gpt-4",  # Reemplaza "gpt-4" con el nombre real del motor de GPT-4
                messages=messages,  
                max_tokens=1000,
                temperature=0
            )
            print(response.choices[0].message.content)
            
            return response.choices[0].message.content.strip()
            
        except Exception as e:  
            print("Error in get_response: " + str(e))
            
    def _get_structure(self, user, query, category):
        try:
            messages = []
            if category in ["4", "5"]:
                if user.age < 15: category += ".1"
                else: category += ".2"
                     
            structure = Prompts().get_prompt("prompts", category) 
            messages = [
                {
                    "role": "system",
                    "content": structure
                }                
            ]
            messages += user.record
            content = [{
                "role" : "user",    
                "content": query
            }]
            messages += content
            return messages
        except Exception as e:
            print("Error in _get_structure: " + str(e))
            
    def get_answer(self, user, query, category):
        try:
            messages = [{"role":"system", "content": "Has de respondre en catalá."}]
            messages += self._get_structure(user, query, category)
            return self.get_response(messages)
        except Exception as e:
            print("Error in get_answer: " + str(e))
    
    def get_classification(self, user, query):
        try:
            messages = self._get_structure(user, query, "classification")
            print(messages)
            return json.loads(self.get_response(messages))
            
        except Exception as e:
            print("Error in get_classification: " + str(e))
        
    def get_disease(self, disease, query):
        try:
            structure = Prompts().get_prompt("prompts", "disease")
            d = Prompts().get_prompt("disease", disease)
            structure += disease + ": Els simptomes son: " + d["sintomas"] + ". Prevencio: " + d["prevencion"] + ". Tractament: " + d["tratamiento"]
            print("Structure: " + structure)
            message = [
                {
                    "role":"system", 
                    "content": structure
                }
            ]
            message += [{"role": "user", "content": query}]
            return self.get_response(message)
             
        except Exception as e:
            print("Error in get_deasea: " + str(e))
        
    def get_protection(self, protecction, query):
        try:
            structure = Prompts().get_prompt("prompts", "disease")
            d = Prompts().get_prompt("protection", protecction)
            structure += "El funcionament es " + d["funcionamiento"] + ", l'eficacia es " + d["eficacia"] + ", els cambis a la regla son " + d["cambios_en_la_regla"] + ", la seva utilitzacio es: " + d["como_se_utiliza"] + ", si es fa un mal us o es trenca: " +  d["mal_uso_o_rotura"] + ", temps sense fertilitat: " + d["tiempo_en_fertilidad"] + ", quan no es pot utilitzar: " + d["cuando_no_utilizarlo"] + ", efectes, neguetius: " + d["efectos_negativos_de_uso"] + ", ventatjes: " +  d["ventajas"] + ", inconvenients: " + d["inconvenientes"] + ", el seu preu es: " + d["precio"]             
            
            print("Structure: " + structure)
            message = [
                {
                    "role":"system", 
                    "content": structure
                }
            ]
            message += [{"role": "user", "content": query}]
            return self.get_response(message)
             
        except Exception as e:
            print("Error in get_protection: " + str(e))