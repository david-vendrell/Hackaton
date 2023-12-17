from controller import Controller
from colorama import init, Fore, Style
from user import UserManager, User
import threading


print(f"\n\n{Fore.YELLOW}***********************\n\nWelcome to Interactive Test V1.0 by Hackaton\n\n***********************\n{Style.RESET_ALL}")
print(f"{Fore.BLUE}Write your name [fede, david, marcos, javi]\n\n{Style.RESET_ALL}")

inp = None
inp = input(f"{Fore.WHITE}Name: {Style.RESET_ALL}")
while inp not in ["javi","marc","david","marcos"]:
    print("TE HAS EQUIVOCADO :( \nEscribe: javi || marc || david || marcos")
    inp = input(f"{Fore.WHITE}Name: {Style.RESET_ALL}")


if inp == "marcos":
    user = User()
    user.id = ""
    user.name =  "marcos"
    user.age = 20
    user.height = 180
    user.gender = "male"
    UserManager().save_user(user)

elif inp == "marc":
    name = "marc"

elif inp == "david":
    user = User()
    user.id = "988592334"
    user.name =  "david"
    user.age = 20
    user.height = 180
    user.gender = "male"
    UserManager().save_user(user)
    

elif inp == "javi":
    name = "javi"
    

while True:
    try:
        linea = input(f"\n{Fore.RED}{inp.capitalize()}:    {Style.RESET_ALL}")
        if not linea:
            break
        
        t = threading.Thread(target=Controller().handle_request, args=(linea, user.name,))
        t.start()
        
    except EOFError:
        break
