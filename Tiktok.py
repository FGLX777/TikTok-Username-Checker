import requests,random,threading,random,time,os
from time import sleep
import colorama
from os import system
from pyutil import filereplace
from colorama import Fore, Style
colorama.init()

#Kinda Cute#0525 <-- Sexy guy
#Dont skid
#FUck this code is ugly 


valid = 0
bad = 0
system("title " + "TikTok Checker Developed by KindaCute/FGLX")
system('mode con: cols=85 lines=20')
msg = Fore.LIGHTMAGENTA_EX+"""
___________.__ __   ___________     __    
\__    ___/|__|  | _\__    ___/___ |  | __
  |    |   |  |  |/ / |    | /  _ \|  |/ /
  |    |   |  |    <  |    |(  <_> )    < 
  |____|   |__|__|_ \ |____| \____/|__|_ |
                   \/                   \/
                   """
print(msg)
print("        ["+Fore.LIGHTWHITE_EX+"https://github.com/FGLX777"+Fore.LIGHTMAGENTA_EX+"]")
print("")
print("╔["+Fore.LIGHTWHITE_EX+"Import Txt"+Fore.LIGHTMAGENTA_EX+"]")
txt = input("╚═"+Fore.LIGHTWHITE_EX+"$"+Fore.LIGHTMAGENTA_EX+"> ")
print("")
print("╔["+Fore.LIGHTWHITE_EX+"Max Letter Length"+Fore.LIGHTMAGENTA_EX+"]")
maxlen = int(input("╚═"+Fore.LIGHTWHITE_EX+"$"+Fore.LIGHTMAGENTA_EX+"> "))
print("")
print("╔["+Fore.LIGHTWHITE_EX+"Threads"+Fore.LIGHTMAGENTA_EX+"]")
thread = int(input("╚═"+Fore.LIGHTWHITE_EX+"$"+Fore.LIGHTMAGENTA_EX+"> "))
os.system("cls")
def check():
    global valid
    global bad
    with open(txt) as f:
            for line in f:
                lines = open(txt).read().splitlines()
                username =random.choice(lines)
                if len(username) <= 4:
                    pass
                elif len(username) >= maxlen:
                    pass
                else:
                    session = requests.Session()
                    system("title " + f"Taken:{bad} Available:{valid}")
                    for x in range(2):
                        r = session.get(f"https://www.tiktok.com/@{username}",headers={"Connection": "Keep-alive","User-Agent": "TikTok 17.4.0 rv:174014 (iPhone; ios 13.6.1; sv_SE) Cronet"})
                    if r.status_code == 404:
                        valid += 1
                        print(Fore.GREEN+"[+]"+Fore.RESET+f"{username}")
                        with open(f"TikTok.txt", "a+") as (k):
                            k.writelines(f"{username}\n")
                    else:
                        bad += 1
                sleep(2)
                        

for x in range(thread):
    x = threading.Thread(target=check)
    x.start()
    sleep(0.2)

