from forums.auto import *
from core.ResultsCollector import resultcollector
import asyncio

class gathered:
    username = []
    profiles = []



def forums_check(dct):
    username = gathered.username
    name=dct["name"]
    url=dct["url"].format(username)
    check_code = dct["check_code"]
    check = dct["check"]
    htext = highlight(url,username)
    
    if(check_code=="1"):
        
        req = urlopen(url,timeout=4)
        try:
            source = req.read().decode("utf-8")
        except:
            source = req.read().decode("latin-1")

        if(check.format(username) in source):
            print(f"{symbol.forum_found} {color.blue}{color.bold}forum/{color.green}{color.bold}{name}{color.reset} : {htext}{color.reset}")
            gathered.profiles.append({name:url})

    elif(check_code=="2"):
        req = urlopen(url,timeout=4)
        st = req.getcode()
        try:
            source = req.read().decode("utf-8")
        except:
            source = req.read().decode("latin-1")

        if(st!=check):
            print(f"{symbol.forum_found} {color.blue}{color.bold}forum/{color.green}{color.bold}{name}{color.reset} : {htext}{color.reset}")
            gathered.profiles.append({name:url})
            #print({name:url})

    elif(check_code=="3"):
        req = urlopen(url,timeout=40)
        #print(req)
        try:
            source = req.read().decode("utf-8")
        except:
            source = req.read().decode("latin-1")
        #print(highlight(text=source, selected=check))
        if(not check in source):
            print(f"{symbol.forum_found} {color.blue}{color.bold}forum/{color.green}{color.bold}{name}{color.reset} : {htext}{color.reset}")
            gathered.profiles.append([name,url])

    



async def focmint(username):
    db = get_db()["forums"]
    tasks = []
    
    for i in range(len(db)):
        try:
            tasks.append(asyncio.create_task(forums_check(db[i])))
        except Exception as e:
            pass
    await asyncio.gather(*tasks)





class forums:
    def run(username):
        print(f"{symbol.log} Searching {color.bold}{color.orange}{username}{color.reset} on {color.bold}Forums{color.reset}...")
        gathered.username = username
        asyncio.run(focmint(username))
        resultcollector.add_result("forums",gathered.profiles)
        print(f"{symbol.log} {color.bold}Forum Search{color.reset} finished. {color.bold}{color.red}{len(gathered.profiles)}{color.reset} results found...")