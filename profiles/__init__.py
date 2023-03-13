########################
#   Social Media Scan  #
########################

from profiles.autoimport import *
from profiles.notapi import notapi
from core.ResultsCollector import resultcollector
import asyncio

async def socmint(username, db_item):
    try:
        cofi = await asyncio.to_thread(notapi, username, db_item)
        if cofi is not None:
            gathered.profiles.append(cofi)
            

            
    except Exception as e:
        pass


async def run_socmint(username):
    db = get_db()
    tasks = []
 
    for i in range(len(db)):
        if db[f"{i}"]["type"] == "notapi":
            tasks.append(asyncio.create_task(socmint(username, db[f"{i}"])))

    await asyncio.gather(*tasks)
    resultcollector.add_result("social",gathered.profiles)
    

class profiles:
    def run(username):
        print(f"{symbol.log} Starting {color.bold}Social Media{color.reset} OSINT for {color.bold}{color.orange}{username}{color.reset}...")
        asyncio.run(run_socmint(username))
        print(f"{symbol.log} {color.bold}Social Media OSINT{color.reset} finished. {color.bold}{color.red}{len(gathered.profiles)}{color.reset} results found...")
    
        resultcollector.add_result("personal",{"Name": gathered.names, "Location": gathered.locations, "Education": gathered.educations, "Bio": gathered.bios, "Linked Urls": gathered.linked_urls, "Phone Numbers": gathered.phone_numbers, "Mails": gathered.mails})
        # print(gathered.names)
        # print(gathered.locations)
        # print(gathered.educations)
        # print(gathered.bios)
        # print(gathered.linked_urls)
        # print(gathered.profiles)
        
        # print(gathered.phone_numbers)
        # print(gathered.mails)