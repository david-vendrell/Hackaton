import openai
import json

from prompts import Prompts

openai.organization = "org-7Xlzvwkj0VnvG7N6xeNY1RN4"
openai.api_key = "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"

class ChatGPT: 

    def get_response(self, messages):
        try:
            response = openai.chat.completions.create(
                model="gpt-4",  # Reemplaza "gpt-4" con el nombre real del motor de GPT-4
                messages=messages,  
                max_tokens=1000,
                temperature=0
            )
            print(response.choices[0].message.content)
            
            return json.loads(response.choices[0].message.content.strip())
            
        except Exception as e:
            print("Error: " + str(e))
            
    def _get_structure(self, user, query, category):
        try:
            structure = Prompts().get_prompt(category)
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
            
        except Exception as e:
            print("Error in _get_structure: " + str(e))
            
    def get_answer(self, user, query, category):
        try:
            messages = self._get_structure(user, query, category)
            return self.get_response(messages)
        except Exception as e:
            print("Error in get_answer: " + str(e))
    
    def get_classification(self, user, query):
        try:
            messages = self._get_structure(user, query, "classification")
            return self.get_response(messages)
            
        except Exception as e:
            print("Error in get_classification: " + str(e))
        
        