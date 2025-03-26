import requests as req
import time as t
from colorama import Fore as F

g = F.GREEN
r = F.RED
c = F.CYAN
re = F.RESET

def main(): # main
    print(f"""{c}
             _     _                                              
 _____     _| |_ _| |_                ____      _     _           
|     |___|   __|   __|___ ___ ___   |    \ ___| |___| |_ ___ ___ 
| | | | -_|__   |__   | .'| . | -_|  |  |  | -_| | -_|  _| -_|  _|
|_|_|_|___|_   _|_   _|__,|_  |___|  |____/|___|_|___|_| |___|_|  
            |_|   |_|     |___|                                   by s0rdeal
""")
    token = input(f'{c}Your Token:{re} ') 
    channelid = input(f'{c}Channel ID:{re} ')
    header = {
        'Authorization':token # auth
    }
    uri = "https://discord.com/api/v9" # base url
    res = req.get(url=f"{uri}/channels/{channelid}/messages",headers=header) 

    channel = res.json() # get messages id

    for messages in channel:
        if messages['author']['id'] == "119554936030756864": # filter
            t.sleep(0.5)
            mres = req.delete(url=f"{uri}/channels/{channelid}/messages/{messages['id']}",headers=header) # delete all messages
            
            if mres.status_code == 204:
                print(f"{g}Message {c}'{messages['content']}'{g} Deleted Successfully{re}") # 204
            else:
                print(f'{r}Error {mres.status_code}: {mres.text}{re}') # ERROR

        else:
            print(".") # filter
main() # start