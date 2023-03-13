import requests 
import json 
import time 
from core.ResultsCollector import resultcollector
from core import (
    banner,
    color,
    symbol,
    clear,
    highlight,
    info_highlight,
    error_highlight,
    css
)

class gathered:
    links = []

def search(value):
    print(f"{symbol.log} Searching {color.bold}{color.orange}{value}{color.reset} on {color.bold}Github Commits{color.reset}...")
        
    req = requests.get(f"https://api.github.com/search/issues?q={value}&type=commits",timeout=25)

    db = json.loads(req.text)
    cnt = db["total_count"]
    data = db["items"]
    out = f"{symbol.github_found}:\n"
    if(cnt!=0):
        for i in range(0,cnt):
            #print(f"{symbol.paste_found} {color.bold}Paste{color.reset} : [{color.red}{color.underline}https://pastebin.com/{data[i]['id']}{color.reset}] {color.bold}Include{color.reset} : {color.reset}[{color.orange}{data[i]['text']}{color.reset}]")
            #time.sleep(4)
            try:
                out+=f"     {color.reset}[{color.whitebg}{data[i]['id']}{color.reset}] {color.bold}URL{color.reset} : [{color.red}{color.underline}https://github.com/{data[i]['url'].split('https://api.github.com/repos/')[1]}{color.reset}] {color.bold}Title{color.reset} : {color.reset}[{color.include}{data[i]['title']}{color.reset}]\n"
                gathered.links.append({str(data[i]['id']):data[i]['url']});
            except:
                pass
    if(len(gathered.links)!=0):
        print(out)
    
    print(f"{symbol.log} Github commit search finished! {color.red}{len(gathered.links)}{color.reset} results found for {color.bold}{color.orange}{value}{color.reset}.")
    
    resultcollector.add_result("github",gathered.links)
    #return gathered.links

