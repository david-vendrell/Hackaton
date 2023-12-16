import json

prompts = {
    "classification": '''
    
    ''',
    
    "its": '''
    
    
    ''',
    "porn": '''
    
    
    ''',
    "anti": '''
    
    
    '''
}

class Prompts:
    def get_prompt(self, key):
        return prompts[key]
        