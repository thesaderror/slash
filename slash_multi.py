import typer
from os import system
import time

from profiles import profiles
from forums import forums 

from core import (
    banner,
    color,
    symbol,
    clear
)
from core.check import *
import threading
import argparse 

from api.pastebin import search as pastesearch
from api.github import search as githubsearch
from api.extract import extract as extract 
from api.leakcheck import check as leakcheck 



def gethelp():
    print(f"""{symbol.help_found}:
    {color.redbg}Slash{color.reset} Includes : 
        {color.bold}paste{color.reset} search
        {color.bold}social media{color.reset} search
        {color.bold}forum{color.reset} search
        {color.bold}leak check{color.reset}

    Example :
    {color.graybg}{color.red}{color.bold}${color.reset}{color.graybg} python slash.py redc86{color.reset}
    {color.graybg}{color.red}{color.bold}${color.reset}{color.graybg} python slash.py target@gmail.com{color.reset}""")

def _username(username):
    print(f"{symbol.log} {symbol.slash} starting...")
    print(f"{symbol.log} Username [{color.green}{color.bold}{username}{color.reset}] succesfully setted.")
    threading.Thread(target=profiles.run,args=(username,)).start()
    threading.Thread(target=forums.run,args=(username,)).start()
    time.sleep(5)
    try:threading.Thread(target=pastesearch,args=(username,)).start()
    except:pass
    try:threading.Thread(target=githubsearch,args=(username,)).start()
    except:pass

def _mail(mail_adress):
    print(f"{symbol.log} {symbol.slash} starting...")
    print(f"{symbol.log} Mail adress [{color.green}{color.bold}{mail_adress}{color.reset}] succesfully setted.")
    
    threading.Thread(target=leakcheck,args=(mail_adress,)).start()
    time.sleep(3)
    threading.Thread(target=pastesearch,args=(mail_adress,)).start()
    threading.Thread(target=githubsearch,args=(mail_adress,)).start()


    
def _start(value : str):

    if(value=="/" or value=="h" or value=='help'):
        gethelp()
    elif(len(extract.just.mail(value))!=0):
        _mail(value)
    elif(len(extract.just.phone(value))!=0):
        pass
    else:
        _username(value)

if __name__ == "__main__":
    clear()
    print(banner.slash)
    #_start()
    typer.run(_start)

# By redc86...