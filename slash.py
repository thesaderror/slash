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
from core.ResultsCollector import resultcollector

import time

def gethelp():
    print(f"""{symbol.help_found}:
    {color.redbg}SlashX{color.reset} Includes : 
        {color.bold}paste{color.reset} search
        {color.bold}social media{color.reset} search
        {color.bold}forum{color.reset} search
        {color.bold}leak check{color.reset}

    Example :
    {color.graybg}{color.red}{color.bold}${color.reset}{color.graybg} python slash.py nuked88{color.reset}
    {color.graybg}{color.red}{color.bold}${color.reset}{color.graybg} python slash.py target@gmail.com{color.reset}""")
 

def _username(username):
    print(f"{symbol.log} {symbol.slash} starting...")
    print(f"{symbol.log} Username [{color.green}{color.bold}{username}{color.reset}] succesfully setted.")
    try:
        start = time.time()

        # Thread list
        threads = [
            threading.Thread(target=profiles.run, args=(username,)),
            threading.Thread(target=forums.run, args=(username,)),
            threading.Thread(target=pastesearch, args=(username,)),
            threading.Thread(target=githubsearch, args=(username,))
        ]

        # Start threads
        for t in threads:
            t.start()

        # Wait for threads to finish
        for t in threads:
            t.join()

        # Save results
        resultcollector.save_results()

        end = time.time()
        print(f"{symbol.log} {symbol.slash} finished in {end-start} seconds.")

    except Exception as e:
        pass



def _mail(mail_adress):
    print(f"{symbol.log} {symbol.slash} starting...")
    print(f"{symbol.log} Mail adress [{color.green}{color.bold}{mail_adress}{color.reset}] succesfully setted.")

    start = time.time()
    # Thread list
    threads = [
        threading.Thread(target=leakcheck, args=(mail_adress,)),
        threading.Thread(target=pastesearch, args=(mail_adress,)),
        threading.Thread(target=githubsearch, args=(mail_adress,))
    ]

    # Start threads
    for t in threads:
        t.start()

    # Wait for threads to finish
    for t in threads:
        t.join()

    # Save results
    resultcollector.save_results()
    
    end = time.time()
    print(f"{symbol.log} {symbol.slash} finished in {end-start} seconds.")




    

    
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
    typer.run(_start)
  



# By redc86...